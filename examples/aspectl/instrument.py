# -*- coding: utf-8 -*-
import aspectlib
import examples.aspectl.bookstore as mod
import examples.aspectl.run as rn
from monitoring.Record import (BeforeOperationEvent,
                               AfterOperationFailedEvent, AfterOperationEvent)
from monitoring.Controller import MonitoringController
import types

monitoring_controller = MonitoringController()
@aspectlib.Aspect(bind=True)
def wrapper(cutpoint, *args, **kwargs):
        print('before')
       
        timestamp = monitoring_controller.time_source_controller.get_time()
        func_module = cutpoint.__module__
        class_signature = cutpoint.__qualname__.split(".", 1)[0]
        monitoring_controller.new_monitoring_record(BeforeOperationEvent(
               timestamp, "before", None, cutpoint.__name__,
               f'{func_module}.{class_signature}'))

        try:
            result = yield aspectlib.Proceed
        except Exception as e:
            print('after failed')
            timestamp = monitoring_controller.time_source_controller.get_time()
            monitoring_controller.new_monitoring_record(
                AfterOperationFailedEvent(timestamp, "after failed",
                                          None, cutpoint.__name__,
                                          f'{func_module}.{class_signature}',
                                          repr(e)))

            raise e
        print('after')
        timestamp = monitoring_controller.time_source_controller.get_time()
        monitoring_controller.new_monitoring_record(AfterOperationEvent(
            timestamp, "after", None, cutpoint.__name__,
            f'{func_module}.{class_signature}'))
        yield aspectlib.Return(result)


@aspectlib.Aspect
def test():
    result = yield 
    yield aspectlib.Return(1)



aspectlib.weave(mod, wrapper)

rn.main()