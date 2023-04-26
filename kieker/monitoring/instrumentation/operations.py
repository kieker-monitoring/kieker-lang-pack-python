# -*- coding: utf-8 -*-
from monitoring.controller import SingleMonitoringController
from monitoring.traceregistry import TraceRegistry
from monitoring.record.trace.operation.operationevent import (BeforeOperationEvent,
                                                              AfterOperationEvent,
                                                              AfterOperationFailedEvent,
                                                              )

monitoring_controller = SingleMonitoringController()  # Singleton
trace_reg = TraceRegistry()


def brefore_operation_event(func):

    # before routine
    trace = trace_reg.get_trace()
    if (trace is None):
        trace = trace_reg.register_trace()

        monitoring_controller.new_monitoring_record(trace)

    trace_id = trace.trace_id
    timestamp = monitoring_controller.time_source_controller.get_time()
    func_module = func.__module__
    class_signature = func.__qualname__.split(".", 1)[0]
    qualname = (func.__module__ if class_signature == func.__name__ else
                f'{func_module}.{class_signature}')

    monitoring_controller.new_monitoring_record(BeforeOperationEvent(
        timestamp, trace_id, trace.get_next_order_id(), func.__name__,
        qualname))


def after_operation_event(func):
    timestamp = monitoring_controller.time_source_controller.get_time()
    trace = trace_reg.get_trace()
    trace_id = trace.trace_id
    func_module = func.__module__
    class_signature = func.__qualname__.split(".", 1)[0]
    qualname = (func.__module__ if class_signature == func.__name__ else
                f'{func_module}.{class_signature}')
    monitoring_controller.new_monitoring_record(AfterOperationEvent(
        timestamp,
        trace_id,
        trace.get_next_order_id(),
        func.__name__,
        qualname))


def after_operation_failed_event(func, exception):
    timestamp = monitoring_controller.time_source_controller.get_time()
    trace = trace_reg.get_trace()
    trace_id = trace.trace_id
    func_module = func.__module__
    class_signature = func.__qualname__.split(".", 1)[0]
    qualname = (func.__module__ if class_signature == func.__name__ else
                f'{func_module}.{class_signature}')
    monitoring_controller.new_monitoring_record(
        AfterOperationFailedEvent(timestamp, trace_id,
                                  trace.get_next_order_id(),
                                  func.__name__,
                                  qualname,
                                  repr(exception)))


def create_deco():
    def decorator(func, args, kwargs):
        ...
