# -*- coding: utf-8 -*-

import examples.automatic.Bookstore
from tools.Aspect import ModuleAspectizer



obj = ModuleAspectizer()
obj.add_module(examples.automatic.Bookstore)

obj.instrumentize()
examples.automatic.Bookstore.Bookstore().search_book()
#x=test4.simplefunction(2)
#print(x)