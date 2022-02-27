# General Setup

No matter which of the approaches bellow you want to use you must always perform following steps.

1. Create a configuration file, where you describe how do you want to use kieker. An example can be found [here](https://github.com/silvergl/kieker-lang-pack-python/blob/refractor2/monitoring.ini)
2. You  must instatiate a `SingleMonitoringControler` object. (This is a singleton class)

In following we assume that `path` as a variable containg a path to the configuration file.

### Invasive Approach
This is the most basic and invasive approach. Currently, it also offers the most control over the instrumentation.
Let's assume that you want to log following function every time it is called.

```python
example.py

def some_function():
      print('Hello World!')

```


```python
example.py

from monitoring.controller import SingleMonitoringController

ctrl = SingleMonitoringController(path)
def some_function():
      print('Hello World!')

```
Now we have everything we need to log the function execution.
At the current stage of development there are three record types with following entries.

- `BeforeOperationEvent`: timestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class
- `AfterOperationEvent`: timestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class
- `AfterOPerationFailedEvent`: timestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class, error name

Create a record object and pass it to the monitoring controler via `new_monitoring_record()`. In our example we use `BeforeExecutionRecord` and `AfterExecutionRecord`.

```python
example.py

from monitoring.controller import SingleMonitoringController
from monitoring.record import (BeforeOperationEvent, AfterOperationEvent)
from monitoring.traceregistry import TraceRegistry

ctrl = SingleMonitoringController()
trace_reg = TraceRegistry()
def some_function():
      trace = trace_reg.get_trace()
        if(trace is None):
            trace = trace_reg.register_trace()
            monitoring_controller.new_monitoring_record(trace)
      trace_id = trace.trace_id
      timestamp = ctrl.time_source_controller.get_time()
      before_record = BeforeOperationevent(timestamp, trace_id, trace.get_next_order_id(), 'some_function','example.some_function')
      ctrl.new_monitoring_record(before_record)
      print('Hello World!')
      timestamp = ctrl.time_source_controller.get_time()
      after_record = AfterOperationEvent(timestamp, trace_id, trace.get_next_order_id(), 'some_function','example.some_function')
      ctrl.new_monitoring_record(after_record)


```
 
 
 ### Semi Invasive Approach
The above method gives us full control over program instrumentation, but it also requieres a lot of manual work. But this approach alters your own code logic, which might not be a problem for small projects, but for larger code basis it becomes a tedious job to keep an overview. To minimize the grade of source code manipulation you can use an `Instrument` decorator. By anotation a function or method with `@Instrument` you can save a lot of typing. Consider the following example.

```python
example.py
from monitoring.controller import SingleMonitoringController
from tools.aspect import instrument

monitoring_controller = SingleMonitoringController(path) # Always instatiate a controller

@instrument
def some_function():
      print('Hello World!')
```

Alternatively, if you want to instrument all class methods at once, you do not have to annotate each function. Instead, set the `__metaclass__` variable of a class to 'Instrumental'


```python
example.py

from tools.Aspect import Instrumental
from monitoring.controller import SingleMonitoringController

monitoring_controller = SingleMonitoringController(path) # Always instatiate a controller
class Foo:
      __metaclass__ = Instrumental
      
      def __init(self):
            pass
      
      def func(self):
            # Do something
            pass
```

As a result, each time a class method or functions are called, Kieker will log automatically. Like in the above example you should get two log files.

## Import Hooks
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

