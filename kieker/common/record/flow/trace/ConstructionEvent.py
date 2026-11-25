# since 1.5
# author Jan Waller

from kieker.common.record.flow.trace.AbstractTraceEvent import (
    AbstractTraceEvent,
)


class ConstructionEvent (AbstractTraceEvent):
    def __init__(self, timestamp, trace_id, order_index, class_signature, object_id):
        super().__init__(timestamp, trace_id, order_index)
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None
            else class_signature)
        self.object_id = object_id

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_string(self.class_signature)
        serializer.put_int(self.object_id)

