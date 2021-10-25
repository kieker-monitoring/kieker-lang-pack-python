import inspect
from monitoring.record import (BeforeOperationEvent,
                               AfterOperationFailedEvent, AfterOperationEvent)
from monitoring.controller import MonitoringController, WriterController
from monitoring.writer import TCPWriter

import types
from monitoring.tcp import TCPClient
#tcp = TCPClient()
monitoring_controller = MonitoringController(WriterController())
def decorate_members(mod):
    # Decorate classes
    #print(f'importing {mod}')
    for name, member in inspect.getmembers(mod, inspect.isclass):
        
        if(member.__module__==mod.__spec__.name):# skip referenced modules
           # print(f'apply decorator for: {name},{member} ')
            for v, k in inspect.getmembers(member, inspect.ismethod):
                if  inspect.isclass(k.__self__):
                    pass
                    #setattr(member, v , instrument_class_method(k))
                else:    
                    setattr(member, v, instrument_method(k))
        #    print('class')
    if mod.__spec__.name =='mainwindow':
        print('skip')
        return
    
    for name, member in inspect.getmembers(mod, inspect.isfunction):
        if(member.__module__==mod.__spec__.name):
            mod.__dict__[name] = instrument(member)


def instrument(func):
    def wrapper(*args, **kwargs):
        # before routine
        timestamp = monitoring_controller.time_source_controller.get_time()
        func_module = func.__module__
        class_signature = func.__qualname__.split(".", 1)[0]
        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
               timestamp, -1, -2, func.__name__,
               f'{func_module}.{class_signature}'))

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # failed routine
            timestamp = monitoring_controller.time_source_controller.get_time()
            monitoring_controller.new_monitoring_record(
                AfterOperationFailedEvent(timestamp, -2,
                                          -1, func.__name__,
                                          f'{func_module}.{class_signature}',
                                          repr(e)))

            raise e
        # after routine
        timestamp = monitoring_controller.time_source_controller.get_time()
        monitoring_controller.new_monitoring_record(AfterOperationEvent(
            timestamp, -2, -1, func.__name__,
            f'{func_module}.{class_signature}'))
        return result
    return wrapper

def instrument_class_method(func):
    def wrapper(*args, **kwargs):
        # before routine
        timestamp = monitoring_controller.time_source_controller.get_time()
        func_module = func.__module__
        class_signature = func.__qualname__.split(".", 1)[0]
        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
               timestamp, -1, -2, func.__name__,
               f'{func_module}.{class_signature}'))

        try:
         
            new_args= list(args)
            if len(new_args)>1:
                new_args = tuple(new_args[1:])
                result = func(*new_args, **kwargs)
            elif len(new_args)==1:
                result = func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
        except Exception as e:
            # failed routine
            timestamp = monitoring_controller.time_source_controller.get_time()
            monitoring_controller.new_monitoring_record(
                AfterOperationFailedEvent(timestamp, -2,
                                          -1, func.__name__,
                                          f'{func_module}.{class_signature}',
                                          repr(e)))

            raise e
        # after routine
        timestamp = monitoring_controller.time_source_controller.get_time()
        monitoring_controller.new_monitoring_record(AfterOperationEvent(
            timestamp, -2, -1, func.__name__,
            f'{func_module}.{class_signature}'))
        return result
    return wrapper

def instrument_method(func):
    def wrapper(self, *args, **kwargs):
        # before routine
        timestamp = monitoring_controller.time_source_controller.get_time()
        func_module = func.__module__
        class_signature = func.__qualname__.split(".", 1)[0]
        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
               timestamp, -1, -2, func.__name__,
               f'{func_module}.{class_signature}'))

        try:
            result = func(self, *args, **kwargs)
        except Exception as e:
            # failed routine
            timestamp = monitoring_controller.time_source_controller.get_time()
            monitoring_controller.new_monitoring_record(
                AfterOperationFailedEvent(timestamp, -2,
                                          -1, func.__name__,
                                          f'{func_module}.{class_signature}',
                                          repr(e)))

            raise e
        # after routine
        timestamp = monitoring_controller.time_source_controller.get_time()
        monitoring_controller.new_monitoring_record(AfterOperationEvent(
            timestamp, -2, -1, func.__name__,
            f'{func_module}.{class_signature}'))
        return result
    return wrapper

def _class_decorator(cls):
    for name, value in inspect.getmembers(cls, lambda x: inspect.isfunction(x) or inspect.ismethod(x)):
        if not name.startswith('__'):
            setattr(cls, name, instrument(value))
    return cls


class Instrumental(type):
    """This metaclass is used for the manual instrumentation"""
    def __new__(cls, name, bases, attr):
        for name, value in attr.items():
            if name == "__init__":
                continue
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attr[name] = test(value)
        return type.__new__(cls, name, bases, attr)


class ModuleAspectizer:
    """This class collects modules and automatically instruments them"""

    def __init__(self):
        self.modules = list()
        self.decorator = instrument

    def add_module(self, module):
        self.modules.append(module)

    def _decorate_module_functions(self):
        if self.decorator is None:
            raise TypeError('No decorator specified!')
        try:
            for module in self.modules:
                for name, member in inspect.getmembers(module):
                    if (inspect.getmodule(member) == module and
                    inspect.isfunction(member)):
                        if(member == self._decorate_module_functions or
                           member == self.decorator):
                            continue
                        module.__dict__[name] = self.decorator(member)
        except (ValueError, TypeError):
            print("No modules to decorate")

    def _decorate_classes(self):
        if self.decorator is None:
            raise TypeError
        try:
            for module in self.modules:
                for name, value in inspect.getmembers(module, inspect.isclass):
                    if(inspect.getmodule(value)==module):
                        if (value ==self):
                            continue
                        setattr(module, name, _class_decorator(value))
        except (ValueError, TypeError):
            print("No modules to decorate")

    def instrumentize(self):
        """ instrumentizes all modules contained in ModuleAspectizer.modules"""
        #self._decorate_module_functions()
        self._decorate_classes()
