# -*- coding: utf-8 -*-

from PyByteBuffer import ByteBuffer
from common import WriterRegistry
from writer import AbstractLogStreamHandler
class BinaryLogStreamHandler(AbstractLogStreamHandler):
    
   def  __init__(self,flush_log_file:bool,
             buffer_size:int, 
             writer_registry:WriterRegistry,serializer):
       super.serializer=serializer
       self.flush_log_file=flush_log_file
       self.buffer_size=buffer_size
       self.writer_registry=writer_registry
       self.buffer=ByteBuffer.allocate(self.buffer_size)
       
    
   def serialize(self,record, identifier):
       self.buffer.put(identifier)
       self.buffer.put(record.getLoggingTimeStamp)
       record.serialize(self.serializer)
  
    def close():
        self.buffer.rewind
    
  
        