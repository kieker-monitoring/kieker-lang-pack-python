# How To Use Kieker For Python
This quick overview shows how to instrument python programs with Kieker.

At the current stage we offer three alternatives of how to achieve it. We can categorize theses approaches by 
how  much you must alter your own source code.

### Invasive Approach
This is the most basic and invasive approach. Currently, it also offers the most control over the instrumentation.
Let's assume that you want to log following function every time it is called.

```python
example.py

def some_function():
      print('Hello World!')

```
First of all, create a `MonitoringController` object and assign it to a global variable. At the current stage of the development
the MonitoringController can be imported from `monitoring.Controller` module. In this example we use `FileWriter` to write the logs to a file.
This writer is instantiated internally by default, so you don't have to specify it expicitly.

```python
example.py

from monitoring.Controller import MonitoringController

ctrl = MonitoringController()
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

from monitoring.Controller import MonitoringController
from monitoring.Record import (BeforeOperationEvent, AfterOperationEvent)

ctrl = MonitoringController()
def some_function():
      timestamp = ctrl.time_source_controller.get_time()
      before_record = BeforeOperationevent(timestamp,-1,-1, 'some_function','example.some_function')
      ctrl.new_monitoring_record(before_record)
      print('Hello World!')
      after_record = AfterOperationEvent(timestamp,-1,-1, 'some_function','example.some_function')
      ctrl.new_monitoring_record(after_record)


```
Note, at that point, we have not implemeted traceId and traceId order API yet, so we passed some dummy value like -1. Generally, both of these entries must be integers.
For finding out the timestamp, we use `time_source_controller`, which is part of `monitoring controller`. But you can use your own method. A timestamp is an integer representing current date in miliseconds.

The `AfterExecutionFailedEvent` record is used in similar manne. Put the original function code in a `try` block and create `AfterExecutionFailedEvent` in the `except` part, passing the error name as the last constructor parameter.
The complete example

```python
example.py

from monitoring.Controller import MonitoringController
from monitoring.Record import (BeforeOperationEvent,
                               AfterOperationFailedEvent, AfterOperationEvent)

ctrl = MonitoringController()
def some_function():
      timestamp = ctrl.time_source_controller.get_time()
      before_record = BeforeOperationEvent(timestamp,-1,-1, 'some_function','example.some_function')
      ctrl.new_monitoring_record(before_record)
      try:         
            print('Hello World!')
      except Exception as e:
            timestamp = monitoring_controller.time_source_controller.get_time()
            failed_record=AfterOperationFailedEvent(timestamp,-1,-1, 'some_function','example.some_function',repr(e))
            ctrl.new_monitoring_record(failed_record)
            raise e
      timestamp = monitoring_controller.time_source_controller.get_time()
      after_record = AfterOperationRecord(timestamp,-1,-1, 'some_function','example.some_function')
      ctrl.new_monitoring_record(after_record)

```

If everything runs as expected, two files will be generated in the directory where you run your program. `Monitoring.log` contains all the records, `Record-map.log` contains inforrmation about which id is assigned to a string in the records.

### Semi Invasive Approach
The above method gives us full control over program instrumentation, but it also requieres a lot of manual work. But this approach alters your own code logic, which might not be a problem for small projects, but for larger code basis it becomes a tedious job to keep an overview. To minimize the grade of source code manipulation you can use an `Instrument` decorator. By anotation a function or method with `@Instrument` you can save a lot of typing. Consider the following example.

```python
example.py

from tools.Aspect import instrument
@instrument
def some_function():
      print('Hello World!')
```

Alternatively, if you want to instrument all class methods at once, you do not have to annotate each function. Instead, set the `__metaclass__` variable of a class to 'Instrumental'


```python
example.py

from tools.Aspect import Instrumental
class Foo:
      __metaclass__ = Instrumental
      
      def __init(self):
            pass
      
      def func(self):
            # Do something
            pass
```

As a result, each time a class method or functions are called, Kieker will log automatically. Like in the above example you should get two log files.

### Non invasive approach
This approach assumes, that there is a certain entrypoint, that starts your program.
You can use this method if you do not want to touch and change the orginal code in any way.

Let's assume that you have a project with some Python modules a and b. So your project structure would look like this:
```
/project_root
   |a.py   
   |b.py
```
Let's also assume that the entrypoint in form of a main function lies in `a.py`.
Now create a new .py file. The name is not important. Let's call it `instrumnet.py` in our example.
In this module import all original modules of your project. Then use our `tool.Aspect` module to instrument them.

```python
instrument.py

import a
import b
from tools.Aspect import ModuleAspectizer

instr = ModuleAspectizer()
obj.add_module(a)
obj.add_module(b)

obj.instrumentize()
a.main()

```
Now you can run instrument.py as starter script and the whole program will be instrumented and executed.

### Summary
