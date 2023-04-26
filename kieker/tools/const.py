import inspect
from monitoring.traceregistry import TraceRegistry
from monitoring.controller import SingleMonitoringController
from tools.ModuleTransformer import ModuleTransformer

### aspect.py ###
trace_reg = TraceRegistry()


def is_method_or_function(x): return inspect.isfunction(
    x) or inspect.ismethod(x)


monitoring_controller = SingleMonitoringController()  # Singleton

### importhookast.py ###
transformer = ModuleTransformer()
