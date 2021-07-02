# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
class AbstractMonitoringWriter(ABC):
      
    @abstractmethod
    def onStarting():
        pass
    
    @abstractmethod
    def  writeMonitoringRecord(self, monitoringRecord):
        pass
    
    @abstractmethod
    def on_terminating(self):
        pass
    @abstractmethod
    def to_string():
       pass
     

from common.records.Serializer import Serializer
       
class FileWriter(AbstractMonitoringWriter):
    def __init__(self, file_path, string_buffer):
        #self.writer_registry=writer_registry
        self.file_path=file_path
        #self.max_entries=max_entries
        self.file=file=open(self.file_path,"x")
        self.string_buffer=string_buffer
        self.serializer=Serializer(self.string_buffer)
    
    
    def writeMonitoringRecord(self, record):
        record.serialize(self.serializer)    
        write_string=''.join(map(str, self.string_buffer))
        self.file.write(write_string)
      
        
    def onStarting():
          pass
    
    def  on_terminating():
        return "finished"
    
    def to_string():
        return "string"
        
        
                    