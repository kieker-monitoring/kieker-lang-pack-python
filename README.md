# README

# Disclaimer 
The Kieker language pack for Python is in an early stage. This means any code in
this repository is not functional or usable in any way other than evaluating how
to implement Python instrumentation.

# Instalation
Prerequisites: 
- python >=3.9
- build package (pip install build)
- 
1. clone this repository
2. cd ./kieker-lang-pack-python
3. run python3 -m build 
4. pip install dist/kieker-monitoring-for-python-0.0.1.tar.gz


# Instrumentation

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

import tools.const as con


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

import const as con
from monitoring.record.trace.operation.operationevent import (BeforeOperationEvent,
                                                              AfterOperationEvent, 
                                                              AfterOperationFailedEvent, 
                                                              )
                           
ctrl = SingleMonitoringController('/path/to/config.ini')



def some_function():
      trace_reg = con.trace_reg
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
from tools.aspect import instrument
from monitoring.controller import SingleMonitoringController

monitoring_controller = SingleMonitoringController('/path/to/config.ini') # Always instatiate a controller

@instrument
def some_function():
      print('Hello World!')
```


## Import Hooks
We also provide two import Hooks. They are used in similar manner. All you have to do is to add either PostImportFinder or InstrumentOnImportFinder to the
sys.meta_path in the module which is a an entry point for your python program.
Bellow we show all the necessary API to do that.

### Post Import Hook

``` python
from tools.importhook import PostImportFinder
from monitoring.controller import SingleMonitoringController


pattern_object = re.compile('YOUR REGEX') # Some regex to describe which modules should be instrumented
exclude_modules = list() # List with explicit strings of modules which should be excluded from the instrumentations
some_var = SingleMonitoringController('/path/to/config.ini')
sys.meta_path.insert(0, PostImportFinder(pattern_object, exclude_modules))

```
  
### Pre Import Hook
```python
import re
from tools.aspect import decorate_find_spec
from tools.importhookast import  InstrumentOnImportFinder

ex=list()
sys.meta_path.insert(0, InstrumentOnImportFinder(ignore_list=ex, empty=False,  debug_on=True))

```
