# -*- coding: utf-8 -*-
import IWriteRegistry
class WriterRegistry(IWriteRegistry) :
    def __init__(self, storage,  identification):
        self.storage=storage
        self.nextId=None
        self.registryListener=None
        self.identification=identification
        
    def getId(self,*args):
        if len(args) == 0:
          return self.identification 
        elif len(args) == 1 and isinstance(args[0], str):
          valueid=self.storage.get(args[0])
          if(valueid == None):
              self.register(args[0])
              return self.storage.get(args[0])
          else:
              return valueid
          
    def register(self,value):
         if value not in self.storage:
             value_id=self.nextId+1
             self.storage.update({'value':value_id})
             #self.registryListener.onNewRegistryEntry(value,value_id)
         