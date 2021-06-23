# -*- coding: utf-8 -*-
from abs import ABS, abstractmethod
class  AbstractLogStreamHandler (ABS):
    
    def __init__(self,flushLogFile,
			  writerRegistry, numOfEntries, numOfBytes,serializer):
        self.flushLogFile = flushLogFile
        self.writerRegistry = writerRegistry
        self.numOfEntries = numOfEntries
        self.numOfBytes = numOfBytes
        self.serializer =serializer
    @abstractmethod
    def serialize(record,identification:int):
         pass
        