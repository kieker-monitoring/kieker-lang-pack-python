# -*- coding: utf-8 -*-
import AbstractController
class TimeSourceController(AbstractController):
    def __init__(self, time_source):
       # super().__init__()
        self.time_source=time_source
      
    def initialize(self):
        pass
    
    def cleanup(self):
        self.debug("shuttig down")
        
    def toString(self):
        pass