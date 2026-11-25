# -*- coding: utf-8 -*-
# Modified by Natalie Kaufhold, 2026

import examples.automatic.Bookstore
from kieker.tools.aspect import ModuleAspectizer



obj = ModuleAspectizer()
obj.add_module(examples.automatic.Bookstore)

obj.instrumentize()

#x=test4.simplefunction(2)
#print(x)
#def run_main():
examples.automatic.Bookstore.main()