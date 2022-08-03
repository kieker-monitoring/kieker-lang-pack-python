# -*- coding: utf-8 -*-
from ast import NodeTransformer, Name, Load

class ModuleTransformer(NodeTransformer):
    def visit_FunctionDef(self, node):
        ''' Add a decorator to the function definition. 
        The decorator is placed at the very bottom to avoid TypeErrors,
        caused by other decorators '''     
        node.decorator_list.append( Name("instrument", ctx=Load()))
        return node
    
