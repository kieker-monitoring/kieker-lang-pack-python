# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
class AbstractMonitoringWriter(ABC):
    def __init__(self):
        pass
    
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
     