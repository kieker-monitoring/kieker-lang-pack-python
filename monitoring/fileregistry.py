# -*- coding: utf-8 -*-

class WriterRegistry:
    
    def __init__(self):
        self.storage={}
        self.next_id=id+1
        self.id=0

    def get_id(self, value):
        idee=self.storage[value]
        if(idee is None):
            self.register(value)
            return self.storage[value]
        return idee
    
    def register(self,value):
        if value not in self.storage:
            idee=self.next_id
            self.storage.update({value,idee})