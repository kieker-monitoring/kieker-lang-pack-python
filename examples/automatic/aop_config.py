# -*- coding: utf-8 -*-

import examples.automatic.Bookstore
from tools.Aspect import ModuleAspectizer



obj = ModuleAspectizer()
obj.add_module(examples.automatic.Bookstore)

obj.instrumentize()

#x=test4.simplefunction(2)
#print(x)
def run_main():
    examples.automatic.Bookstore.main()