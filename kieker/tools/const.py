import inspect

# Modified by Natalie Kaufhold, 2026
from kieker.monitoring.traceregistry import TraceRegistry
from kieker.monitoring.controller import MonitoringController
from kieker.tools.ModuleTransformer import ModuleTransformer

# For aspect.py
trace_reg = TraceRegistry()


def is_method_or_function(x):
    return inspect.isfunction(x) or inspect.ismethod(x)


monitoring_controller = MonitoringController()  # Singleton

# For importhookast.py
transformer = ModuleTransformer()
