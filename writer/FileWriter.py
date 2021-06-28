# -*- coding: utf-8 -*-
import AbstractMonitoringWriter
from records import Serializer
class FileWriter(AbstractMonitoringWriter):
    def __init__(self,writer_registry, max_entries, log_stream_handler, file_path,string_buffer):
        self.writer_registry=writer_registry
        self.file_path=file_path
        self.max_entries=max_entries
        self.file=file=open(self.file_path,"x")
        self.string_buffer=string_buffer
        self.serializer=Serializer(self.string_buffer)
    def writeMonitoringRecord(self, record):
        if self.log_stream_handler.num_entries>=self.max_entries:

            pass
        
        recordClassName="Some class" #dummyvalue
        record.serialize(self.serializer)
        f=open(self.file_path,"x")
        write_string=map(''.join(map(str, self.string_buffer)))
        f.write(write_string)
      
       #lf.writer_registry.register(recordClassName)
        
    def onStarting():
          pass
    
    def  on_terminating():
        return "finished"
    
    def to_string():
        return "string"
        
        
            