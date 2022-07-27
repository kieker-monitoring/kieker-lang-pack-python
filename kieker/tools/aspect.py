import inspect
import types
import decorator
import sys

from monitoring.record.trace.operation.operationevent import (BeforeOperationEvent,
                                                              AfterOperationEvent, 
                                                              AfterOperationFailedEvent, 
                                                              )
from monitoring.controller import SingleMonitoringController
from monitoring.traceregistry import TraceRegistry



monitoring_controller = SingleMonitoringController() #Singleton
trace_reg = TraceRegistry()


@decorator.decorator
def instrument(func,*args, **kwargs):
    # before routine
    trace = trace_reg.get_trace()
    new_trace = trace is None
    if new_trace:
        trace = trace_reg.register_trace()      
        monitoring_controller.new_monitoring_record(trace)
        
    # before routine
    trace_id = trace.trace_id
    timestamp = monitoring_controller.time_source_controller.get_time()
    func_module = func.__module__
    class_signature = func.__qualname__.split(".", 1)[0]
    qualname = (func.__module__ if class_signature == func.__name__ else
                f'{func_module}.{class_signature}')
    
    monitoring_controller.new_monitoring_record(BeforeOperationEvent(
           timestamp, trace_id, trace.get_next_order_id(), func.__name__,
           qualname))
    

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
    finally:
        if new_trace:
            trace_reg.unregister_trace()
    # after routine
    timestamp = monitoring_controller.time_source_controller.get_time()
    
    monitoring_controller.new_monitoring_record(AfterOperationEvent(
        timestamp,
        trace_id,
        trace.get_next_order_id(),
        func.__name__,
        qualname))
   
    return result



is_method_or_function = lambda x: inspect.isfunction(x) or inspect.ismethod(x)
def decorate_members(mod):
    '''
    Decorates methods and global functions of the given module
    '''
    #class_redecorator = redecorate(instrument)
    # Decorate classes
    for name, member in inspect.getmembers(mod, inspect.isclass):
        if(member.__module__ == mod.__spec__.name):  # skip members of immported modules
            for k, v in inspect.getmembers(member, is_method_or_function):
                try:
                  
                    if isinstance(member.__dict__[k], classmethod):
                        funcobj=member.__dict__[k].__func__
                        setattr(member, k, classmethod(instrument(funcobj)))
                    elif isinstance(member.__dict__[k], staticmethod):
                        funcobj=member.__dict__[k].__func__
                        setattr(member, k, staticmethod(instrument(funcobj)))
                        pass
                    elif isinstance(member.__dict__[k], property):
                       #functions = property
                        funcobj=member.__dict__[k].__func__
                        setattr(member, k, property(instrument(funcobj)))      
                        pass
                    elif isinstance(member.__dict__[k], types.FunctionType):
                      #  funcobj = inspect.unwrap(v)
                        setattr(member, k, instrument(v))
                        pass
                    #setattr(ember, k , functions (funcobj)
                except KeyError:
                    # inspect.getmembers() lists also methods from inherited
                    # classes. __dict__ contains information about methods that
                    # are defined in the given class. So, do nothing 
                    # and continue
                    continue
                    

    for name, member in inspect.getmembers(mod, inspect.isfunction):
        if(member.__module__ == mod.__spec__.name):
            mod.__dict__[name] = instrument(member)
    
    

@decorator.decorator
def decorate_find_spec(find_spec, module_name=None,exclusion=None, *args, **kwargs):
   # print(args[1])
    result = find_spec(*args, **kwargs)
    if result is None:
       # print("fdss")
        return None
    #print(result)
    try:
      #  assert not result is None 
        if "exec_module" in dir(result.loader):
     #       print("d")
            exec_module = getattr(result.loader, "exec_module")
            if isinstance(exec_module, classmethod):
                funcobj = exec_module.__func__
                setattr(result.loader, "exec_module",classmethod(decorate_create_or_load_module(funcobj, module_name, exclusion)))
            elif isinstance(exec_module, types.MethodType):
	            funcobj = exec_module.__func__
	            #rint(print(type(getattr(finder, "find_spec"))))
	            setattr(result.loader, "exec_module", types.MethodType(decorate_create_or_load_module(funcobj, module_name, exclusion), result.loader))
            else:
                setattr(result.loader, "exec_module", decorate_create_or_load_module(exec_module, module_name, exclusion))
    except AssertionError:
        return result
    return result

@decorator.decorator
def decorate_create_or_load_module(exec_module, module_name=None, exclusion=None, *args, **kwargs):
   
    exec_module(*args, **kwargs)
    if exclusion in args[1].__spec__.name or args[1].__spec__.name in exclusion:
        return
    elif module_name in args[1].__spec__.name:
        decorate_members(sys.modules[args[1].__spec__.name])
    

###############################################################################
# DEPRECATED AND NOT USED FUNCTIONS, BUT STILL MIGHT BE USEFUL                #
###############################################################################

# Deprecated
def redecorate(redecorator):
    ''' Originally posted here:
    https://stackoverflow.com/a/9540553/12558231
    '''
    def wrapper(f, flag):
        info = (f, None)
        if (isinstance(f, classmethod)):
            info = (f.__func__, classmethod)
        elif (isinstance(f, staticmethod)):
            info = (f.__func__, staticmethod)
        elif (isinstance(f, property)):
            info = (f.fget, property)

        if (info[1] is not None):
            return info[1](redecorator(info[0], flag))
        return redecorator(info[0], flag)
    return wrapper

def isclassmethod(method): # We do not use it anymore, but might be useful again
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
