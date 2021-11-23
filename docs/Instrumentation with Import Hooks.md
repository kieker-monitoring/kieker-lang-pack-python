# Import Hooks
Import Hook is a technique in python, that allows us to modify import behavior of the python modules.
This feature allows us to instrument the program with barely any source code modification. 
Unlike any other approach described [ here ], we do not even have to specify the locations of the code that we like to instrument. 

There are two ways of how we can achieve it, depending on what python version we want to use. However, we describe for now the deprecated approach.
Although this approach is officially deprecated, it is still supported by python. Newer  approach might be not backwards compatible.

We must implement the following two classes:


```python

class PostImportFinder:
    def __init__(self):
        self._skip=set()
    
    def find_module(self, fullname, path = None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self)


class PostImportLoader:
    def __init__(self, finder):
        self._finder = finder
    
    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        if 'package_root' in fullname and 'manager' not in fullname:
                decorate_members(module)
        self._finder._skip.remove(fullname)
        return module
```
The most important part is the if-statement in `load module()` method. We check if 'package_root' is part of the fully qualified name of the module. 
Note that `'package_root'` can be any other value depending on what you would like to instrument. For example, we used 'spyder' while testing  the instrumentation 
with spyder-ide , since fully-qualified names of all modules start with 'spyder.' . We can also exclude some modules from instrumentation, by ensuring, their name is not a part
of fully-qulified name of the module to be loaded.

After we ensured that we atrget the correct module, we simply call a function named 'decorate_members', that accepts module object as an argument. 


