# -*- coding: utf-8 -*-
# Modified by Natalie Kaufhold, November 2026

import socket as s
import errno
import os
import threading
from datetime import datetime, timezone
from monitoring.util import TimeStamp, get_prefix
from struct import pack
from monitoring.serialization import Serializer, BinarySerializer
from monitoring.fileregistry import WriterRegistry
from configparser import ConfigParser


MAX_FILE_SIZE = 5 * 1024 * 1024


class DummyWriter:
    ''' This writer, is used to simulate writing, no records are written '''

    def __init__(self):
        pass

    def on_new_registry_entry(self, value, idee):
        pass

    def writeMonitoringRecord(self, record):
        pass

    def _serialize(self, record, idee):
        pass

    def onStarting(self):
        pass

    def on_terminating(self):
        pass

    def to_string(self):
        pass


class FileWriter:
    ''' This writer, is used to write the records directly into local files. It gets the file_path of the created log files. '''

    def __init__(self, file_path, string_buffer):
        # Ensure the wanted directory is actually created, iff it does not exist already.
        os.makedirs(file_path, exist_ok=True)
        self.base_path = file_path
        self.string_buffer = string_buffer
        self.serializer = Serializer(self.string_buffer)
        self.writer_registry = WriterRegistry(self)
        self._file_lock = threading.Lock()
        self._day = None
        self._file_number = 0
        self._create_new_file(datetime.now(timezone.utc))

    def _create_new_file(self, timestamp):
        day = timestamp.strftime('%Y-%m-%d')
        day_changed = day != self._day
        if day_changed:
            self._day = day
            self._file_number = 0

        day_directory = os.path.join(self.base_path, day)
        os.makedirs(day_directory, exist_ok=True)
        self._update_latest_link(day)
        if day_changed:
            # This way the mapping file is written in all log-dirs.
            self.map_file_writer = MappingFileWriter(day_directory)
            for event_type, event_id in self.writer_registry.storage.items():
                self.map_file_writer.add(event_id, event_type)
        time = timestamp.strftime('%H-%M-%S')

        while True:
            self._file_number += 1
            filename = (
                f"kieker-{day}-{time}-UTC-{self._file_number}.dat")
            file_path = os.path.join(day_directory, filename)
            try:
                with open(file_path, 'x'):
                    pass
            except FileExistsError:
                continue
            self.file_path = file_path
            return

    def _update_latest_link(self, day):
        latest_path = os.path.join(self.base_path, 'latest')
        if os.path.islink(latest_path):
            if os.readlink(latest_path) == day:
                return
            os.unlink(latest_path)
        elif os.path.lexists(latest_path):
            raise FileExistsError(
                f"Cannot create latest link: {latest_path} already exists.")

        os.symlink(day, latest_path)

    def on_new_registry_entry(self, value, Id):
        self.map_file_writer.add(Id, value)

    def writeMonitoringRecord(self, record):
        __module = record.__class__.__module__
        __qualname = record.__class__.__qualname__
        record_class_name = __module + __qualname
        self.writer_registry.register(record_class_name)
        self._serialize(record, self.writer_registry.get_id(record_class_name))

    def _serialize(self, record, idee):
        with self._file_lock:
            timestamp = datetime.now(timezone.utc)
            if timestamp.strftime('%Y-%m-%d') != self._day:
                self._create_new_file(timestamp)

            header = f'{idee};'
            self.string_buffer.append(header)
            record.serialize(self.serializer)
            write_string = '$' + ''.join(map(str, self.string_buffer)) + '\n'
            self.string_buffer.clear()
            with open(self.file_path, 'a') as file:
                file.write(write_string)
                file.close()

            if os.path.getsize(self.file_path) > MAX_FILE_SIZE:
                self._create_new_file(datetime.now(timezone.utc))

    def onStarting(self):
        pass

    def on_terminating(self):
        pass

    def to_string(self):
        pass


class MappingFileWriter:
    ''' Creates a file, which maps the type of event to an corresponding id. '''

    def __init__(self, file_path):
        self.file_path = os.path.join(file_path, 'kieker.map')

    def add(self, Id, class_name):
        with open(self.file_path, 'a') as file:
            file.write(f'${Id}={class_name}\n')


lock = threading.Lock()

time = TimeStamp()


class TCPWriter:
    ''' Sends the record data to a remote data collector. '''

    def __init__(self, config):
        config_parser = ConfigParser()
        config_parser.read(config)
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        # !!enable multiconnection on the collector and sender!!
        self.multConnections = config_parser.getboolean(
            'General', 'multiple_Connections')
        self.host = config_parser.get('Tcp', 'host')
        self.port = config_parser.getint('Tcp', 'port')
        self.connetction_timeout = config_parser.getint(
            'Tcp', 'connection_timeout')
        self.max_retries = 1000000
        if not self.multConnections:
            for attempt in range(1, self.max_retries + 1):
                ret = self.socket.connect_ex((self.host, self.port))
                if ret == 0:
                    break
                elif ret == errno.ECONNREFUSED:
                    continue
                else:
                    print(f"Connection failed with {os.strerror(ret)}. Aborting.")
                    break
        self.writer_registry = WriterRegistry(self)
        self.serializer = BinarySerializer([], self.writer_registry)

    def on_new_registry_entry(self, value, idee):
        # int - id, int-length, bytesequences
        # encode value in utf-8 and pack it with the id
        # value should be always a string
        v_encode = str(value).encode('utf-8')
        format_string = f'!iii{len(v_encode)}s'
        result = pack(format_string, -1, idee, len(v_encode), v_encode)
        try:
            if self.multConnections:
                self.socket.connect_ex((self.host, self.port))
                self.socket.sendall(result)
                self.socket.close()
            else:
                self.socket.sendall(result)
        except Exception as e:
            print(repr(e))  # TODO: better exception handling

    def writeMonitoringRecord(self, record):
        # fetch record name
        lock.acquire()
        record_class_name = record.__class__.__name__
        prefix = get_prefix(record_class_name)
        record_class_name = prefix + record_class_name
        # register class name and append it to the sent record
        self.writer_registry.register(record_class_name)
        self.serializer.put_string(record_class_name)
        self.serializer.put_long(time.get_time())
        # send record
        record.serialize(self.serializer)
        binarized_record = self.serializer.pack()
        lock.release()
        # try to send
        try:
            if self.multConnections:
                self.socket.connect_ex((self.host, self.port))
                self.socket.sendall(binarized_record)
                self.socket.close()
            else:
                self.socket.sendall(binarized_record)
        except Exception as e:
            # TODO: Better exception handling for tcp
            print(repr(e))

    def on_terminating(self):
        # TODO
        pass
