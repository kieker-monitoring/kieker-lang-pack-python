# since 1.6
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IConstructorRecord import IConstructorRecord
from common.record.flow.trace.operation.CallOperationEvent import (
    CallOperationEvent,
)


class CallConstructorEvent (CallOperationEvent, IConstructorRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature):
        super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature)

    def serialize(self, serializer):
        super().serialize(serializer)

