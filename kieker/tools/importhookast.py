#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:24:25 2022

@author: serafim
"""

from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location
from ast import ImportFrom,  parse, alias, unparse, fix_missing_locations
import os
import const as con




class InstrumentOnImportFinder(MetaPathFinder):
         
    def __init__(self, ignore_list = [], debug_on = False):
        self.debug_on = debug_on
        self.ignore_list = ignore_list
        
    def find_spec(self, fullname, path, target = None):
        name = fullname.split(".")[-1]
        if path is None or path == "":
            path = [os.getcwd()]
        for e in path:
            directory = os.path.join(e, name)
            if os.path.isdir(directory):
                filename = os.path.join(directory, "__init__.py")
                spec = spec_from_file_location(fullname,
                                               filename,
                                               loader=InstLoader(filename, self.ignore_list, self.debug_on), 
                                               submodule_search_locations=[directory])
            else:
                filename = directory + ".py"
                spec = spec_from_file_location(fullname,
                                               filename,
                                               loader=InstLoader(filename, self.ignore_list, self.debug_on), 
                                               submodule_search_locations=None)
            
            if  os.path.exists(filename):
                return spec
            else:
                del spec 
        return None
    
    
class InstLoader(Loader):
    def __init__(self, filename, ignore_list, debug=False):
        self.filename = filename
        self.debug_on = debug
        self.ignore_list = ignore_list
        

    def create_module(self, spec):
        return None 

    def exec_module(self, module):
       # Read module source code
       with open(self.filename) as f:
           data = f.read()
       # If the module should not be instrumented
       # execute it normally
       if module.__name__ in self.ignore_list: 
          exec(data, vars(module))
          return
       # parse and inject import of tools.aspect
       node = parse(data)
       import_node = ImportFrom(module="tools.aspect", names=[alias(name="instrument")], level=0)

       counter = 0
       for i in node.body:
           if isinstance(i, ImportFrom):
              if i.module == "__future__":
                  counter += 1
           else:
               break
       node.body.insert(counter,import_node)
       
       # Add @instrument annotation
       node = con.transformer.visit(node)
       fix_missing_locations(node)
       data = unparse(node)

       try:  
         if self.debug_on:
             # TODO: create log file o.s.
             print(module.__name__)
         exec(data, vars(module))
       
       except:
           # TODO: Meaningfull exeception handling if any needed
           pass
          
          

    
    
    