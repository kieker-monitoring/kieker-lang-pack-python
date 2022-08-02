#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:24:25 2022

@author: serafim
"""

from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location
from importlib import invalidate_caches
from importlib.abc import SourceLoader
from importlib.machinery import FileFinder
from ast import ImportFrom, Import, parse, alias, unparse, fix_missing_locations
from tools.ModuleTransformer import ModuleTransformer
import os
import sys
import copy
import threading


class MyMetaFinder(MetaPathFinder):
    ''' Original implementation provided here https://stackoverflow.com/a/43573798/12558231 
         by User Dunes. 
         https://creativecommons.org/licenses/by-sa/3.0/ 
         Defintion of "create_module () was modified. '''
         
    def __init__(self, ignore_list={}, debug_on = False):
        self.debug_on = debug_on
        self.ignore_list = ignore_list
        
    def find_spec(self, fullname, path, target=None):
        if path is None or path == "":
            path = [os.getcwd()] # Keep it
        # Can make without if else. Need only name.
        if "." in fullname:
            *parents, name = fullname.split(".")
        else:
            name = fullname
            
        for entry in path: # Rearrange
            if os.path.isdir(os.path.join(entry, name)):
                
                filename = os.path.join(entry, name, "__init__.py")
                submodule_locations = [os.path.join(entry, name)] 
                # spec = spec_from_file_location(fullname, filename, loader=MyLoader(filename),
                #    submodule_search_locations=submodule_locations)
            else:
                filename = os.path.join(entry, name + ".py")
                submodule_locations = None
                # spec = spec_from_file_location(fullname, filename, loader=MyLoader(filename),
                #    submodule_search_locations=submodule_locations)
           # if  os.path.exists(filename):
               # return spec
           
            ### do no need. Delete 
            #if not os.path.exists(filename):
            #    continue
            
          #  return spec_from_file_location(fullname, filename, loader=MyLoader(filename),
           ##     submodule_search_locations=submodule_locations)
        return None
class MyLoader(Loader):
    def __init__(self, filename, ignore_list, debug=False):
        self.filename = filename
        self.debug_on = debug
        self.ignore_list = ignore_list

    def create_module(self, spec):
        return None 

    def exec_module(self, module):
      
           
       with open(self.filename) as f:
           data = f.read()
       node = parse(data)
       ex=["tensorflow.core.framework.tensor_shape_pb2",
           "google.protobuf.descriptor",
           "tensorflow.python.ops.gen_data_flow_ops",
           "tensorflow.compiler.tf2xla.ops.gen_xla_ops",
           "tensorflow.python.platform.device_context",
           "tensorflow.python.util.all_util",
           "tensorflow.python.data.ops.readers",
           "tensorflow.python.autograph.utils",
           "tensorflow.python.data.experimental.ops.interleave_ops"
           
]
       if module.__name__ in ex: # replace with ignore_list
           exec(data, vars(module))
           return
       # Keep original?
       node_copy= copy.deepcopy(node)
       node_copy = unparse(node_copy)
       
       import_node = ImportFrom(module="tools.aspect", names=[alias(name="instrument")], level=0)
       
       # has_import = any(isinstance(x, Import) for x in node.body)
       # has_import_from = any(isinstance(x, ImportFrom) for x in node.body)
       indices = []
       for i in range(len(node.body)):
           if isinstance(node.body[i], ImportFrom):
              if node.body[i].module =="__future__":
                 indices.append(i)
       if indices:
           node.body.insert(max(indices)+1,import_node) 
       else:
           node.body.insert(0,import_node)
       transformer = ModuleTransformer()
       node = transformer.visit(node)
       fix_missing_locations(node)
       data=unparse(node)


       try:  
       
        exec(data, vars(module))
        if self.debug_on:
            print(module.__name__)
       except:
           # TODO: Meaningfull exeception handling
           pass
          
          
loader_details = MyLoader, [".py"]

def install():
    # insert the path hook ahead of other path hooks
    sys.path_hooks.insert(0, FileFinder.path_hook(loader_details))
    # clear any loaders that might already be in use by the FileFinder
    sys.path_importer_cache.clear()
    invalidate_caches()
    
    
    
    