# since 1.6
# author Jan Waller

from kieker.common.record.flow.IObjectRecord import IObjectRecord
from kieker.common.record.flow.trace.operation.constructor.BeforeConstructorEvent import (
    BeforeConstructorEvent,
)


class BeforeConstructorObjectEvent (BeforeConstructorEvent, IObjectRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id):
        super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature)
        self.object_id = object_id

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_int(self.object_id) 

