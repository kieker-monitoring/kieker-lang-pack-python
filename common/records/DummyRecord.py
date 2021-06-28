# -*- coding: utf-8 -*-

class DummyRecord:
    
    def __init__(self, foo_parameter, bar_parameter,serializer):
        self.serializer=serializer
        self.foo_parameter=foo_parameter
        self.bar_parameter=bar_parameter
       
   
    def serialize(self,serializer):
        self.serializer.serialize.put(self.foo_parameter)
        self.serializer.serialize.put(self.bar_parameter)