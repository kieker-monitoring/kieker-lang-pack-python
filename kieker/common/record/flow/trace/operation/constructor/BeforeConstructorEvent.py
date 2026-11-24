# since 1.6
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IConstructorRecord import IConstructorRecord
from common.record.flow.trace.operation.BeforeOperationEvent import (
    BeforeOperationEvent,
)


class BeforeConstructorEvent (BeforeOperationEvent, IConstructorRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature):
        super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature)

    def serialize(self, serializer):
        super().serialize(serializer)

