# -*- coding: utf-8 -*-

class DummyRecord:
    
    def __init__(self, foo_parameter, bar_parameter):
       # self.serializer=serializer
        self.foo_parameter=foo_parameter
        self.bar_parameter=bar_parameter
       
   
    def serialize(self,serializer):
        serializer.put(self.foo_parameter)
        serializer.put(self.bar_parameter)