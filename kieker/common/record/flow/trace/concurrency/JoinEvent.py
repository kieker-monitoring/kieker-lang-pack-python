# since 1.8
# author Jan Waller

from kieker.common.record.flow.trace.AbstractTraceEvent import (
    AbstractTraceEvent,
)


class JoinEvent (AbstractTraceEvent):
    def __init__(self, timestamp, trace_id, order_index, joined_trace_id):
        super().__init__(timestamp, trace_id, order_index)
        self.joined_trace_id = joined_trace_id

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_long(self.joined_trace_id) 

