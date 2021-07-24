import inspect
from monitoring.Record import (TraceMetadata, BeforeOperationEvent,
                               AfterOperationFailedEvent, AfterOperationEvent)
from monitoring.Controller import MonitoringController
import time
import calendar

def instrument(func):
    def wrapper(*args, **kwargs):
        monitoring_controller = MonitoringController()
        timestamp=calendar.timegm(time.gmtime())
        class_signature=func.__self__.__class__
        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
            time.ctime(timestamp)), 42,42,func.__name__, class_signature )
        try:
            result=func(*args, **kwargs)
        except Exception as e:
            monitoring_controller.new_monitoring_record(AfterOperationFailedEvent(
            time.ctime(timestamp)), 42, 42, func.__name__, 
            class_signature, repr(e)))
            raise e
         monitoring_controller.new_monitoring_record(AfterOperationEvent(
            time.ctime(timestamp)), 42,42,func.__name__, class_signature )
        return result
    return wrapper

class Instrumental:
    def __new__(cls, name, bases, local_dict):
        for attr in local_dict:
            if callable(local_dict[attr]):
                local_dict[attr] = instrument(local_dict[attr])
        return type.__new__(cls, name, bases, local_dict)

class ModuleAspectizer:
    def __init__(self,decorator):
        self.modules = list()
        self.classes = list()
        self.decorator = mydecorator
        self.functions = list()

    def add_module(self, module):
        self.modules.append(module)

    def decorate_module_functions(self):
        if self.decorator is None:
            raise TypeError
        try:
            for module in self.modules:
                for name, member in inspect.getmembers(module):
                    if (inspect.getmodule(member) == module and
                    inspect.isfunction(member)):
                        if(member == self.decorate_module_functions or
                           member == self.decorator):
                            continue
                        module.__dict__[name] = self.decorator(member)
        except (ValueError, TypeError):
            print("No modules to decorate")

    def decorate_class_methods(self):
        if self.decorator is None:
            raise TypeError
        try:
            for module in self.modules:
                for name, member in inspect.getmembers(module):
                    if (inspect.getmodule(member) == module and
                        inspect.isclass(member)):
                        for key, value in member.__dict__.items():
                            if inspect.ismethod(value):
                                member.__dict__[key] = self.decorator(value)
        except (ValueError, TypeError):
            print("No modules to decorate")


class ClassAspectizer:
    def __init__(self):
        self.classes = list()
        self.decorator = None
        pass

    def add_class(self, clazz):
        self.classes.append(clazz)

    def decorate_class_members(self):
        if self.decorator is None:
            raise TypeError


class CustomAspectizer:
    # TODO MAYBE
    pass
