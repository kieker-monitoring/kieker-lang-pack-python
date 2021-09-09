# -*- coding: utf-8 -*-
from  monitoring.Controller import MappingFileWriter
class WriterRegistry:
    
    def __init__(self, listner):
        self.storage = {}
        self.id = 0
        self.next_id = self.id+1
        self.listner = listner
        

    def get_id(self, value):
        idee=self.storage[value]
        if(idee is None):
            self.register(value)
            return self.storage[value]
        return idee
    
    def register(self,value):
        if value not in self.storage:
            idee=self.next_id
            self.next_id+=1
            self.storage.update({value: idee})


class SimpleRegistryListener:
    def __init__(self):
        self.map_file_wirter = MappingFileWriter()
        
    
    def on_new_registry_entry(self, value, Id):
        self.map_file_wirter.add(value,Id)
        