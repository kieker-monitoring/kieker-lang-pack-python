# since 1.5
# author Jan Waller

from kieker.common.record.flow.IOperationRecord import IOperationRecord
from kieker.common.record.flow.trace.AbstractTraceEvent import (
    AbstractTraceEvent,
)


class AbstractOperationEvent (AbstractTraceEvent, IOperationRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature):
        super().__init__(timestamp, trace_id, order_index)
        self.operation_signature = (self.OPERATION_SIGNATURE
            if operation_signature is None
            else operation_signature)
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None
            else class_signature)

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_string(self.operation_signature)
        serializer.put_string(self.class_signature)

