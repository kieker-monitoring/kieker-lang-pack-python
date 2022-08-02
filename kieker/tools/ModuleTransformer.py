# -*- coding: utf-8 -*-
from ast import NodeTransformer, Name, Load

class ModuleTransformer(NodeTransformer):
    def visit_FunctionDef(self, node):
     #   self.generic_visit(node)
       # x = node.decorator_list
        clazz = False        	
        if not node.name == "instrument" :
            for d in node.decorator_list:
              if (isinstance(d, Name)):
              #  print("true")
                if (d.id=="classmethod" or d.id=="staticmethod" or
                    d.id=="property" ):
                    clazz = True   
                  #  print(clazz)
            
            if clazz:
                node.decorator_list.append(Name("instrument", ctx=Load()))
            else:
          
              node.decorator_list.append( Name("instrument", ctx=Load()))
        return node
    
