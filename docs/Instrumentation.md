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
 
