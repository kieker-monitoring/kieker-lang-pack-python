# Documentation
This quick overview shows hot to instrument python programs with Kieker.

At the current stage we offer three alternatives of how to achieve it. We can categorize theses approaches by 
how  much  you must alter your own source code.

### Invasive Approach
This is the most basic and  invasive approach. Currently, it also offers the most controll over the instrumentazation.
Let's assume that you want to log following function every time it is called.

```python
example.py

def some_function():
      print('Hello World!')

```
First of all, create a  `MonitoringController` object and assign it to a global variable. At the current stage of the development
the MonitoringController can be imported from `monitoring.Controller` module. In this example we use `FileWriter` to write the logs to a file.
This writer is instatiated internally by default, so you don't have to specify it expicitly.

```python
example.py

from monitoring.Controller import MonitoringController

ctrl = MonitoringController()
def some_function():
      print('Hello World!')

```
Now we have everything we need to log the function execution.
At the current stage of development there are three record types with following entries.

- `BeforeExecutionEvent`: timestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class
- `AfterExecutionEvent`:  imestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class
- `AfterExecutionFailedEvent`: imestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class, error name

Create a record object and pass it to monitoring controler via `new_monitoring_record()`. In our example we use BeforeExecutionRecord and AfterExecutionRecord.

```python
example.py

from monitoring.Controller import MonitoringController

ctrl = MonitoringController()
def some_function():
      timestamp = monitoring_controller.time_source_controller.get_time()
      before_record = BeforeExecutioneRecord(timestamp,-1,-1, 'some_function','example.some_function')
      ctr.new_monitoring_record(before_record)
      print('Hello World!')
      after_record = AfterExecutioneRecord(timestamp,-1,-1, 'some_function','example.some_function')
      ctr.new_monitoring_record(after_record)


```
Note, at that point, we have not implemeted traceId and traceId order API yet, so we passedd some dummy value like -1. Generelly, bot of these entries must be integers.
For finding out the timestamp we use `time_source_controller`, which is part of `monitoring controller`. But you can use your own method. A timestam is an Integer representing current date in miliseconds.

AfterExecutionFailedEvent record is used in similar manne. Put the original function code in try block and create AfterExecutionFailedEvent in except part, passing error name as the last constructor parameter.
The complete example

```python
example.py

from monitoring.Controller import MonitoringController

ctrl = MonitoringController()
def some_function():
      timestamp = monitoring_controller.time_source_controller.get_time()
      before_record = BeforeExecutioneRecord(timestamp,-1,-1, 'some_function','example.some_function')
      ctr.new_monitoring_record(before_record)
      try:         
            print('Hello World!')
      except Exception as e:
            timestamp = monitoring_controller.time_source_controller.get_time()
            failed_record=AfterFailedEvent(timestamp,-1,-1, 'some_function','example.some_function',repr(e))
            ctr.new_monitoring_record(failed_record)
            raise e
      timestamp = monitoring_controller.time_source_controller.get_time()
      after_record = AfterExecutioneRecord(timestamp,-1,-1, 'some_function','example.some_function')
      ctr.new_monitoring_record(after_record)

```


### Semi Invasive Approach
If you don't want to manipulate your code to much,
you can simply use a decorator @instrument from tools.Apsect module, we have prepared.
```python
example.py

from tools.Aspect import Instrumental, instrument
@instrument
def some_function():
      pass
class Foo:
      __metaclass__ = Instrumental
      pass
```
### Non invasive approach
This approach assumes, that there is a certain entrypoint, that starts your programm.
We prepared a script instrument-kieker.py. It accepts a path to a .py file where you can specify 
modules of yur program, which should be instrumentized.
Create an instance of ModuleAspectizer. This class, has a method add_module that accepts a module object.
Add all modules, that must be inspected with kieker. 
Define a method named run_main(), which should simply run entrypoint of your program.

If you don't want to use our non-invasive approach, you can use a third-party lib aspectlib.
In principle it works in the same manner. 
Specify own wrapper function, which creates all necessary records when target function is called
Use aspectlib.weave(target, wrapper) to instrument the code.
Run your entry point.
