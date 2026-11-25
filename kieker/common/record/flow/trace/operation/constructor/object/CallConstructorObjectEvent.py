# since 1.6
# author Jan Waller

from kieker.common.record.flow.ICallObjectRecord import ICallObjectRecord
from kieker.common.record.flow.trace.operation.constructor.CallConstructorEvent import (
    CallConstructorEvent,
)


class CallConstructorObjectEvent (CallConstructorEvent, ICallObjectRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature, object_id, callee_object_id):
        super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature)
        self.object_id = object_id
        self.callee_object_id = callee_object_id

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_int(self.object_id)
        serializer.put_int(self.callee_object_id)

