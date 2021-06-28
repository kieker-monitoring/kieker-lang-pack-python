# -*- coding: utf-8 -*-
import AbstractMonitoringWriter
from records import Serializer
class FileWriter(AbstractMonitoringWriter):
    def __init__(self,writer_registry, max_entries, log_stream_handler, file_path,string_buffer):
        #self.writer_registry=writer_registry
        self.file_path=file_path
        #self.max_entries=max_entries
        self.file=file=open(self.file_path,"x")
        self.string_buffer=string_buffer
        self.serializer=Serializer(self.string_buffer)
    
    
    def writeMonitoringRecord(self, record):
        record.serialize(self.serializer)    
        write_string=map(''.join(map(str, self.string_buffer)))
        self.file.write(write_string)
      
        
    def onStarting():
          pass
    
    def  on_terminating():
        return "finished"
    
    def to_string():
        return "string"
        
        
            