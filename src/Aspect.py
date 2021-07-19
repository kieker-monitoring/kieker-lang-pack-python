import inspect


class ModuleAspectizer:
    def __init__(self):
        self.modules = list()
        self.classes = list()
        self.decorator = None
        self.functions = list()

    def add_module(self, module):
        self.modules.append(module)
   
    def decorate_module_functions(self):
        if self.decorator is None:
            raise TypeError
        try:
            for module in self.modules:
                for name, member in inspect.getmember(module):
                    if (inspect.getmodule(member) == module and
                        inspect.isfunction(member)):
                        if(member == self.decorate_module or
                           member == self.decorator):
                            continue
                        module.__dict__[name]=self.decorator(member)
        except (ValueError, TypeError):
            print("No modules to decorate")

      def decorate_class_methods(self):
          if self.decorator is None:
            raise TypeError
        try:
            for module in self.modules:
                for name, member in inspect.getmember(module):
                    if (inspect.getmodule(member) == module and
                        inspect.isclass(member)):
                        for key, value in member.__dict__.items():
                            if inspect.ismethod(value):
                                member.__dict__[key]=self.decorator(value)
        except (ValueError, TypeError):
            print("No modules to decorate")

class ClassAspectizer:
    def __init__(self):
        self.classes=list()
        self.decorator=None
        pass
    
    def add_class(self, clazz):
        self.classes.append(clazz)
    
    def decorate_class_members(self):
        if self.decorator is None:
            raise TypeError


class CustomAspectizer:
    #TODO MAYBE
    pass
