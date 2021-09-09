# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


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


from monitoring.Record import Serializer
from monitoring.fileregistry import WriterRegistry


class FileWriter(AbstractMonitoringWriter):

    def __init__(self, file_path, string_buffer):
        self.file_path = file_path
        self.string_buffer = string_buffer
        self.serializer = Serializer(self.string_buffer)
        self.writer_registry = WriterRegistry()

    def writeMonitoringRecord(self, record):
        record_class_name = record.__class__.__name__
        self.writer_registry.register(record_class_name)
        self._serialize(record, self.writer_registry.get_id(record_class_name))

    def _serialize(self, record, idee):
        header = f'{idee};'
        self.string_buffer.append(header)
        record.serialize(self.serializer)
        write_string = ''.join(map(str, self.string_buffer))
        self.string_buffer.clear()
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
    def __init__(self,file_path):
        self.file_path = file_path
    
    def add(self, Id, class_name):
        file = open(self.file_path, 'a')
        write_string = f'$ {Id} = {class_name} \n'
        file.write(write_string)
        file.close()

import socket
import logging


class TCPWriter:

    def __init__(self, host, port, buffer, connection_timeout):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = buffer
        self.connetction_timeout = connection_timeout
        self.serializer = Serializer(self.buffer)
        self.onStarting()

    def onStarting(self):
        while True:
            result = self._try_connect_()
            if result:
                break

    def _try_connect_(self):
        try:
            self.socket.connect((self.host, self.port))
            return True
        except socket.timeout as e:
            logging.error(e)
            return False
        except socket.error as e:
            logging.error(e)
            return False

    def writeMonitoringRecord(self, record):
        record.serialize(self.serializer)
        write_string = str.encode(''.join(map(str, self.buffer)),
                                  'utf-8')
        self.socket.sendall(write_string)

    def on_terminating(self):
        pass

    def to_string(self):
        pass
