# -*- coding: utf-8 -*-

# IF WE INSTANTIATE A SOCKET INSIDE OF A CLASS
# THE DATA IS NOT SENT FOR SOME REASEON.
# THIS IS A TERRIBLE SOLUTION BUT
# WE KEEP IT FOR NOW: FIX AS SOON AS POSSIBLE.
#import socket
from struct import pack
from monitoring.tcp import TCPClient
from monitoring.util import TimeStamp, get_prefix
from monitoring.record import Serializer, BinarySerializer
from monitoring.fileregistry import WriterRegistry

time = TimeStamp()
class TCPWriter:
    TCP = TCPClient()
    def __init__(self, host, port, buffer, connection_timeout):
        self.host = host
        self.port = port
        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.socket.connect((self.host, self.port))
        self.TCP.set_port_and_host(self.port, self.host)
        self.TCP.connect()
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
            self.TCP.send(result)
        except Exception as e:
            print(repr(e))  # TODO: better exception handling

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
            self.TCP.send(binarized_record)
        except Exception as e:
            # TODO: Better exception handling for tcp
            print(repr(e))

    def on_terminating(self):
        # TODO ?
        pass

    def to_string(self):
        # TODO ?
        pass