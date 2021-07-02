# -*- coding: utf-8 -*-

class Serializer:
    def __init__(self,string_byte):
        self.string_byte=string_byte
        
    def put(self,value):
           self.string_byte.append(value+"; ")
class DummyRecord:
    
    def __init__(self, foo_parameter, bar_parameter):
       # self.serializer=serializer
        self.foo_parameter=foo_parameter
        self.bar_parameter=bar_parameter
       
   
    def serialize(self,serializer):
        serializer.put(self.foo_parameter)
        serializer.put(self.bar_parameter)