import inspect
from monitoring.record import (BeforeOperationEvent,
                               AfterOperationFailedEvent, AfterOperationEvent)
from monitoring.controller import SingleMonitoringController, WriterController
import types
from monitoring.traceregistry import TraceRegistry
import functools
import decorator

monitoring_controller = SingleMonitoringController()  # Singleton
trace_reg = TraceRegistry()


@decorator.decorator
def instrument1(func, *args, **kwargs):
    # before routine
    trace = trace_reg.get_trace()
    if trace is None:
        trace = trace_reg.register_trace()

        monitoring_controller.new_monitoring_record(trace)

    trace_id = trace.trace_id
    timestamp = monitoring_controller.time_source_controller.get_time()
    func_module = func.__module__
    class_signature = func.__qualname__.split(".", 1)[0]
    qualname = (func.__module__ if class_signature == func.__name__ else
                f'{func_module}.{class_signature}')
    # class_signature = func.__class__.__name__

    monitoring_controller.new_monitoring_record(BeforeOperationEvent(
        timestamp, trace_id, trace.get_next_order_id(), func.__name__,
        qualname))
    # print(f'{func.__name__}, {qualname}')

    try:
        result = func(*args, **kwargs)

    except Exception as e:
        # failed routine

        timestamp = monitoring_controller.time_source_controller.get_time()

        monitoring_controller.new_monitoring_record(
            AfterOperationFailedEvent(timestamp, trace_id,
                                      trace.get_next_order_id(),
                                      func.__name__,
                                      qualname,
                                      repr(e)))

        raise
        # after routine
    timestamp = monitoring_controller.time_source_controller.get_time()

    monitoring_controller.new_monitoring_record(AfterOperationEvent(
        timestamp,
        trace_id,
        trace.get_next_order_id(),
        func.__name__,
        qualname))

    return result


def isclassmethod(method):  # We do not use it anymore, but might be useful again
    bound_to = getattr(method, '__self__', None)
    if not isinstance(bound_to, type):
        # must be bound to a class
        return False
    name = method.__name__
    for cls in bound_to.__mro__:
        descriptor = vars(cls).get(name)
        if descriptor is not None:
            return isinstance(descriptor, classmethod)
    return False


is_method_or_function = lambda x: inspect.isfunction(x) or inspect.ismethod(x)


def decorate_members(mod):
    """
    Decorates methods and global functions of the given module
    """
    # class_redecorator = redecorate(instrument)
    # Decorate classes
    for name, member in inspect.getmembers(mod, inspect.isclass):
        if member.__module__ == mod.__spec__.name:  # skip members of imported modules
            for k, v in inspect.getmembers(member, is_method_or_function):
                try:
                    if "__" in k:  # or k=="call":
                        if k != "__call__" and k != "__init__":
                            continue
                    if isinstance(member.__dict__[k], classmethod):
                        funcobj = member.__dict__[k].__func__
                        setattr(member, k, classmethod(instrument1(funcobj)))
                    elif isinstance(member.__dict__[k], staticmethod):
                        funcobj = member.__dict__[k].__func__
                        setattr(member, k, staticmethod(instrument1(funcobj)))
                        pass
                    elif isinstance(member.__dict__[k], property):
                        funcobj = member.__dict__[k].__func__
                        setattr(member, k, property(instrument1(funcobj)))
                        pass
                    else:
                        #  funcobj = inspect.unwrap(v)
                        setattr(member, k, instrument1(v))
                        pass
                except KeyError:
                    # inspect.getmembers() lists also methods from inherited
                    # classes. __dict__ contains information about methods that
                    # are defined in the given class. So, do nothing 
                    # and continue
                    continue

    for name, member in inspect.getmembers(mod, inspect.isfunction):
        if member.__module__ == mod.__spec__.name:
            mod.__dict__[name] = instrument_function(member, False)


def instrument(func, is_class_method=False):
    """
    Decorator that instruments global functions and methods.
    ---------------
    is_class_method: bool
        Set to true if the method is annotated with @classmethod
        Default is False
        
        If used manually, simply put '@instrument' under the @classmethod
        annotation. 
    """

    @functools.wraps(func)
    def in_wrapper(*args, **kwargs):
        # before routine
        trace = trace_reg.get_trace()
        if trace is None:
            trace = trace_reg.register_trace()

            monitoring_controller.new_monitoring_record(trace)

        trace_id = trace.trace_id
        timestamp = monitoring_controller.time_source_controller.get_time()
        func_module = func.__module__
        class_signature = func.__qualname__.split(".", 1)[0]
        qualname = (func.__module__ if class_signature == func.__name__ else
                    f'{func_module}.{class_signature}')
        # class_signature = func.__class__.__name__

        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
            timestamp, trace_id, trace.get_next_order_id(), func.__name__,
            qualname))

        #    print(f'{func.__name__}, {qualname}')

        try:
            result = func(*args, **kwargs)

        except Exception as e:
            # failed routine
            timestamp = monitoring_controller.time_source_controller.get_time()

            monitoring_controller.new_monitoring_record(
                AfterOperationFailedEvent(timestamp, trace_id,
                                          trace.get_next_order_id(),
                                          func.__name__,
                                          qualname,
                                          repr(e)))

            raise
            # after routine
        timestamp = monitoring_controller.time_source_controller.get_time()

        monitoring_controller.new_monitoring_record(AfterOperationEvent(
            timestamp,
            trace_id,
            trace.get_next_order_id(),
            func.__name__,
            qualname))

        return result

    return in_wrapper


def instrument_function(func, is_class_method=False):
    """
    Decorator that instruments global functions and methods.
    ---------------
    is_class_method: bool
        Set to true if the method is annotated with @classmethod
        Default is False
        if is_class_method:
            result = func( *args, **kwargs)
        else:
        If used manually, simply put '@instrument' under the @classmethod
        annotation. 
    """

    @functools.wraps(func)
    def in_wrapper2(*args, **kwargs):
        # before routine
        trace = trace_reg.get_trace()
        if trace is None:
            trace = trace_reg.register_trace()

            monitoring_controller.new_monitoring_record(trace)

        trace_id = trace.trace_id
        timestamp = monitoring_controller.time_source_controller.get_time()
        func_module = func.__module__
        class_signature = func.__qualname__.split(".", 1)[0]
        qualname = (func.__module__ if class_signature == func.__name__ else
                    f'{func_module}.{class_signature}')
        # class_signature = func.__class__.__name__

        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
            timestamp, trace_id, trace.get_next_order_id(), func.__name__,
            qualname))

        #    print(f'{func.__name__}, {qualname}')

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # failed routine

            timestamp = monitoring_controller.time_source_controller.get_time()

            monitoring_controller.new_monitoring_record(
                AfterOperationFailedEvent(timestamp, trace_id,
                                          trace.get_next_order_id(),
                                          func.__name__,
                                          qualname,
                                          repr(e)))

            raise e
        # after routine
        timestamp = monitoring_controller.time_source_controller.get_time()

        monitoring_controller.new_monitoring_record(AfterOperationEvent(
            timestamp,
            trace_id,
            trace.get_next_order_id(),
            func.__name__,
            qualname))

        return result

    return in_wrapper2


def redecorate(redecorator):
    """ 
    Originally posted here:
    https://stackoverflow.com/a/9540553/12558231
    """

    def wrapper(f, flag):
        info = (f, None)
        if isinstance(f, classmethod):
            info = (f.__func__, classmethod)
        elif isinstance(f, staticmethod):
            info = (f.__func__, staticmethod)
        elif isinstance(f, property):
            info = (f.fget, property)

        if info[1] is not None:
            return info[1](redecorator(info[0], flag))
        return redecorator(info[0], flag)

    return wrapper


def _class_decorator(cls):
    for name, value in inspect.getmembers(cls, lambda x: inspect.isfunction(x) or inspect.ismethod(x)):
        if not name.startswith('__'):
            setattr(cls, name, instrument(value))
    return cls


class Instrumental(type):
    """This metaclass is used for the manual instrumentation"""

    def __new__(mcs, name, bases, attr):
        for name, value in attr.items():
            if name == "__init__":
                continue
            if (isinstance(value, types.FunctionType) or
                    isinstance(value, types.MethodType)):
                attr[name] = instrument(value, False)
        return type.__new__(mcs, name, bases, attr)
