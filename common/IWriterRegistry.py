# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IWriterRegistry(ABC):
    
    @abstractmethod
    def getId(self,*args):
        pass