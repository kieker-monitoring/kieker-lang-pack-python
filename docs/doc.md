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
the MonitoringController class is imported from `monitoring.Controller` module. In this example we use `FileWriter` to write the logs to a file.
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

`BeforeExecutionRecord`: timestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class
`AfterExecutionRecord`:  imestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class
`AfterExecutionFailedRecord`: imestamp in ms, traceId, traceOrder, function_name, fully qualified name of caller class, error name



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
