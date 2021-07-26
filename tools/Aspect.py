import inspect
from monitoring.Record import (TraceMetadata, BeforeOperationEvent,
                               AfterOperationFailedEvent, AfterOperationEvent)
from monitoring.Controller import MonitoringController
import time
import calendar
import types


def instrument(func):
    def wrapper(*args, **kwargs):
        print('before') 
        monitoring_controller = MonitoringController()
        timestamp = calendar.timegm(time.gmtime())
        class_signature = func.__class__        
        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
            time.ctime(timestamp), "before", 42, func.__name__, class_signature ))
        
        try:
            result=func(*args, **kwargs)
        except Exception as e:
            print('after failed')
            timestamp = calendar.timegm(time.gmtime())
            monitoring_controller.new_monitoring_record(AfterOperationFailedEvent(
            time.ctime(timestamp), "after failed", 42, func.__name__,
            class_signature, repr(e)))
            
            raise e
        print ('after')
        monitoring_controller.new_monitoring_record(AfterOperationEvent(
        time.ctime(timestamp), "after",42,func.__name__, class_signature ))
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
                attr[name] = instrument(value)
        return type.__new__(cls, name, bases, attr)


class ModuleAspectizer:
    """This class collects modules and automatically instruments them"""
    def __init__(self):
        self.modules = list()
        self.classes = list()
        self.decorator = instrument
        self.functions = list()

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
                    setattr(module, name, _class_decorator(value))
        except (ValueError, TypeError):
            print("No modules to decorate")

    def instrumentize(self):
        """ instrumentizes all modules contained in ModuleAspectizer.modules"""
        self._decorate_module_functions()
        self._decorate_classes()

