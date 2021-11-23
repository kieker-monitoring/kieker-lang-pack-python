
import importlib
import sys
from tools.aspect import decorate_members
class PostImportFinder:
    def __init__(self, param, exclusions):
        self._skip=set()
        self.param = param
        self. exclusions = exclusions
    
    def find_module(self, fullname, path = None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self, self.param, self.exclusions)


class PostImportLoader:
    def __init__(self, finder, param, exclusions):
        self._finder = finder
        self.param = param
        self.exclusions = exclusions
        
    
    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        if self.param in fullname :
            for ex in self.exclusions:
                if ex in fullname:
                    return
            decorate_members(module)
        self._finder._skip.remove(fullname)
        return module
