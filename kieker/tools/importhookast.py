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
         
    def __init__(self, ignore_list=[], debug_on=False):
        self.debug_on = debug_on
        self.ignore_list = ignore_list
        
    def find_spec(self, fullname, path, target=None):
        
        name = fullname.split(".")[-1]
        
        if path is None or path == "":
            path = [os.getcwd()] 
    
        
        for e in path: # Rearrange
            directory = os.path.join(e, name)
            if os.path.isdir(directory):
                
                filename = os.path.join(directory, "__init__.py")
                submods = [directory] 
                spec = spec_from_file_location(fullname,
                                               filename,
                                               loader=MyLoader(filename, self.ignore_list, self.debug_on), 
                                               submodule_search_locations=submods)
            else:
                filename = directory + ".py"
                submods = None
                spec = spec_from_file_location(fullname,
                                               filename,
                                               loader=MyLoader(filename, self.ignore_list, self.debug_on), 
                                               submodule_search_locations=submods)
            
            if  os.path.exists(filename):
                return spec
            else:
                del spec
           
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
       ex=[#"tensorflow.core.framework.tensor_shape_pb2",
           "google.protobuf.descriptor",
          # "tensorflow.python.ops.gen_data_flow_ops",
        #   "tensorflow.compiler.tf2xla.ops.gen_xla_ops",
          # "tensorflow.python.platform.device_context",
         #  "tensorflow.python.util.all_util",
           #"tensorflow.python.data.ops.readers",
          # "tensorflow.python.autograph.utils",
           # "tensorflow.python.data.experimental.ops.interleave_ops"
           
]
     #  ex = ["tensorflow.python.platform.resource_loader",
      #       "tensorflow.python.eager.backprop",
       #      "tensorflow.python.ops.gen_array_ops",
        #     "tensorflow.python.framework.ops",
         #    "tensorflow.api.ops_eager_execution"]
       if module.__name__ in self.ignore_list: # replace with ignore_list
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
         if self.debug_on:
             print(module.__name__)
         exec(data, vars(module))
       
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
    
    
    
    