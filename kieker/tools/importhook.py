import importlib
import os
import sys
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location
from tools.aspect import decorate_members

# sys.meta_path = MyLIst(sys.MetaPath)


class PostImportFinder:

    def __init__(self, param, exclusions, empty=False):
        self._skip = set()
        self.param = param
        self.exclusions = exclusions
        self.empty = empty

    def find_module(self, fullname, path=None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self, self.param, self.exclusions, self.empty,
                                fullname, "")

    def find_spec(self, fullname, path, target=None):
        name = fullname.split(".")[-1]
        if path is None or path == "":
            path = [os.getcwd()]
        for e in path:
            directory = os.path.join(e, name)

        if fullname in self._skip:
            return None
        self._skip.add(fullname)

        if os.path.isdir(directory):
            filename = os.path.join(directory, "__init__.py")
            spec = spec_from_file_location(
                fullname,
                filename,
                loader=PostImportLoader(self, self.param, self.exclusions,
                                        self.empty, fullname, filename),
                submodule_search_locations=[directory])
        else:
            filename = directory + ".py"
            spec = spec_from_file_location(
                fullname,
                filename,
                loader=PostImportLoader(self, self.param, self.exclusions,
                                        self.empty, fullname, filename),
                submodule_search_locations=None)
        if os.path.exists(filename):
            return spec
        else:
            del spec
        return None


class PostImportLoader:

    def __init__(self, finder, param, exclusions, empty, fullname, filename):
        self.fullname = fullname
        self.filename = filename
        self._finder = finder
        self.param = param
        self.exclusions = exclusions
        self.empty = empty

    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        if self.param.search(fullname) is not None:

            # for ex in self.exclusions:
            #    if ex.match(fullname):
            #       return
            decorate_members(module, self.empty)
        self._finder._skip.remove(fullname)
        return module

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        with open(self.filename) as f:
            data = f.read()
        code_obj = compile(data, filename=self.filename, mode="exec")
        exec(code_obj, vars(module))
        decorate_members(module, self.empty)
        self._finder._skip.remove(self.fullname)
