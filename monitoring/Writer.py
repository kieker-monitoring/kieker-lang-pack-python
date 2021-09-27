# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from monitoring.Record import Serializer, BinarySerializer
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
        header = f'{idee};'
        self.string_buffer.append(header)
        record.serialize(self.serializer)
        write_string = ''.join(map(str, self.string_buffer))+'\n'
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
tcp = TCPClient()
class TCPWriter:

    def __init__(self, host, port, buffer, connection_timeout):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = buffer
        self.registry_buffer = []
        self.connetction_timeout = connection_timeout
       # self.onStarting()
        #self.tcp = TCPClient()
        self.writer_registry = WriterRegistry(self)
        self.serializer = BinarySerializer(self.buffer, self.writer_registry)

    def on_new_registry_entry(self, value, idee):
        # int - id, int-length, bytesequences
        v_encode = str(value).encode('utf-8')
        print(f'len: {len(v_encode)}')
        format_string = f'!iii{len(v_encode)}s'
        result = pack(format_string, -1, idee, len(v_encode), v_encode)
        print(f'map: {result}')
        try:
            tcp.send(result)
        except Exception as e:
            print(repr(e))
    def onStarting(self):
        while True:
            result = self._try_connect_()
            if result:
                break

    def _try_connect_(self):
        try:
            self.socket.connect((self.host, self.port))
            self.socket.sendall(str.encode("Hello World!"))
            return True
        except socket.timeout as e:
            logging.error(e)
            return False
        except socket.error as e:
            logging.error(e)
            return False

    def writeMonitoringRecord(self, record):
        record_class_name = (record.__class__.__module__
                             +record.__class__.__qualname__)
        self.writer_registry.register(record_class_name)
        self.serializer.put_string(record_class_name)
        self.serializer.put_long(record.timestamp)
        record.serialize(self.serializer)
        binarized_record = self.serializer.pack()
        print(f'record: {binarized_record}')
        try:
            tcp.send(binarized_record)
        except Exception as e:
            print(repr(e))
            pass
    def on_terminating(self):
        pass

    def to_string(self):
        pass
