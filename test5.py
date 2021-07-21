# -*- coding: utf-8 -*-
import test4
from src.Aspect import ModuleAspectizer

def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        result=func(*args, **kwargs)
        print (result)
        print("world")
        return result
    return wrapper


obj = ModuleAspectizer(mydecorator)
obj.add_module(test4)

obj.decorate_module_functions()
obj.decorate_class_methods()

#x=test4.simplefunction(2)
#print(x)