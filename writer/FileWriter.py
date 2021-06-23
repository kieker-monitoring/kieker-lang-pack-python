# -*- coding: utf-8 -*-
import AbstractMonitoringWriter
class FileWriter(AbstractMonitoringWriter):
    def __init__(self,writer_registry, max_entries, log_stream_handler):
        self.writer_registry=writer_registry
        self.log_stream_handler=log_stream_handler
        self.max_entries=max_entries
    def writeMonitoringRecord(self, record):
        if self.log_stream_handler.num_entries>=self.max_entries:
            #TODO create file
            pass
        
        recordClassName="Some class" #dummyvalue
        
        self.writer_registry.register(recordClassName)
            
    def onStarting():
          pass
    
    def  on_terminating():
        return "finished"
    
    def to_string():
        return "string"
        
        
            