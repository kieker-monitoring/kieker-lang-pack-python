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

Currently we provide an API to instrument a program with only a few lines of code.
This approach assumes, that there is some entry point of a program. And that the project is structerd in a certain way ().

```python

some_main.py
from tools.importhook import PostImportFinder
from monitoring.controller import SingleMonitoringController

some_var = SingleMonitoringController(path) # always instatiate a controller
my_list = list() # can be empty. Contains a list of module names, that must be skipped and not instrumented
sys.meta_path.insert(0,PostImportFinder('root_name', my_list)) # first parameter is a root name of the modules e.g root_name.something.fancy
```
`sys.meta_path.insert(0,PostImportFinder('root_name', my_list))` instruments the whole program. 

If for some reason our API does not match your need you can implement an import hook yourself.
There are two ways of how we can achieve it, depending on what python version we want to use. 
We provide a description of this technique for the older python versions (3.5).
This approach will also work with the newer versions.


We must implement the following two classes:


```python

import importlib
import sys
from tools.aspect import decorate_members

class PostImportFinder:
    def __init__(self, exclusions):
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
        
        # HERE PUT YOUR LOGIC THAT DESCRIVES WHICH MODULES MUST BE INSTRUMENTED
        # USUALLY YOU WOULD FILTER module dict accordingly.
        # After that call something like:
        # decorate_members(module)
        # That will apply the decorators programatically to the module functions
        self._finder._skip.remove(fullname)
        return module
```


At the end you use your own import hook un the same way it was explained above.



