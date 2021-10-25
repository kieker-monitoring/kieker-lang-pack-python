# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from monitoring.record import Serializer, BinarySerializer
from monitoring.fileregistry import WriterRegistry

class AbstractMonitoringWriter(ABC):

    @abstractmethod
    def onStarting():
        pass

    @abstractmethod
    def writeMonitoringRecord(self, monitoringRecord):
        pass

    @abstractmethod
    def on_terminating(self):
        pass

    @abstractmethod
    def to_string():
        pass


class FileWriter(AbstractMonitoringWriter):

    def __init__(self, file_path, string_buffer):
        self.file_path = file_path
        self.string_buffer = string_buffer
        self.serializer = Serializer(self.string_buffer)
        self.writer_registry = WriterRegistry(self)
        self.map_file_wirter = MappingFileWriter()

    def on_new_registry_entry(self, value, idee):
        self.map_file_wirter.add(value, idee)

    def writeMonitoringRecord(self, record):
        record_class_name = record.__class__.__module__+record.__class__.__qualname__
        self.writer_registry.register(record_class_name)
        self._serialize(record, self.writer_registry.get_id(record_class_name))

    def _serialize(self, record, idee):
        # fetch record line
        header = f'{idee};'
        self.string_buffer.append(header)
        record.serialize(self.serializer)
        write_string = ''.join(map(str, self.string_buffer))+'\n'
        # clear buffer
        self.string_buffer.clear()
        # write to the file
        file = open(self.file_path, 'a')
        file.write(write_string)
        file.close()

    def onStarting(self):
        pass

    def on_terminating(self):
        return "finished"

    def to_string(self):
        return "string"


class MappingFileWriter:
    def __init__(self):
        self.file_path = './record-map.log'

    def add(self, Id, class_name):
        file = open(self.file_path, 'a')
        write_string = f'$ {Id} = {class_name} \n'
        file.write(write_string)
        file.close()


import socket
import logging
from struct import pack
from monitoring.tcp import TCPClient
from monitoring.util import TimeStamp, get_prefix
tcp = TCPClient()
time = TimeStamp()
class TCPWriter:

    def __init__(self, host, port, buffer, connection_timeout):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = buffer
        self.registry_buffer = []
        self.connetction_timeout = connection_timeout
        self.writer_registry = WriterRegistry(self)
        self.serializer = BinarySerializer(self.buffer, self.writer_registry)

    def on_new_registry_entry(self, value, idee):
        # int - id, int-length, bytesequences
        # encode value in utf-8 and pack it with the id
        v_encode = str(value).encode('utf-8')
        format_string = f'!iii{len(v_encode)}s'
        result = pack(format_string, -1, idee, len(v_encode), v_encode)        
        try:
            tcp.send(result)
        except Exception as e:
            print(repr(e)) # TODO: better exception handling

    def writeMonitoringRecord(self, record):
        # fetch record name
        record_class_name = record.__class__.__name__
        java_prefix = get_prefix(record_class_name)
        record_class_name = java_prefix + record_class_name
        # register class name and append it to the sent record
        self.writer_registry.register(record_class_name)
        self.serializer.put_string(record_class_name)
        self.serializer.put_long(time.get_time())
        # send record
        record.serialize(self.serializer)
        binarized_record = self.serializer.pack()
        # try to send
        try:
            tcp.send(binarized_record)
        except Exception as e:
            # TODO: Better exception handling for tcp
            print(repr(e))
            
    def on_terminating(self):
        pass

    def to_string(self):
        pass
