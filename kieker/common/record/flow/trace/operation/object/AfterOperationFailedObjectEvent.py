# since 1.6
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IObjectRecord import IObjectRecord
from common.record.flow.trace.operation.AfterOperationFailedEvent import (
    AfterOperationFailedEvent,
)


class AfterOperationFailedObjectEvent (AfterOperationFailedEvent, IObjectRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, cause, object_id):
        super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, cause)
        self.object_id = object_id

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_int(self.object_id)

