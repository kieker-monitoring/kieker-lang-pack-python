# Documentation
This quick overview shows hot to instrument python programs with Kieker.
At the current stage there are three ways how to do it.

### Invasive Manual Approach
If you want a full controll, you can create records manually.
First of all create a  MonitoringController instance, which must be global.
After that, create a record andpass it to monitoring_controller via "new_monitoring_record

```python
example.py

from monitoring.Controller import MonitoringController
monit_cont = MonitoringController()
def some_function():
      record = BeforeExecutionRecord(timestamp, 1, 2, ''some_function,
               example.some_function'
                                     )
      pass
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
