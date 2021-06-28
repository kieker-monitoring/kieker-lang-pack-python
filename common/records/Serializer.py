# -*- coding: utf-8 -*-

class Serailizer:
    def __init__(self,string_byte):
        self.string_byte=string_byte
        
    def put(self,value):
           self.string_byte.append(value+"; ")
