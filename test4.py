# -*- coding: utf-8 -*-

class Test:
    def __init__(self):
        self.x=1
        pass
    
    def myfunc(self):
        print (self.x)
        
     
obj=Test()
test=obj.myfunc
test()