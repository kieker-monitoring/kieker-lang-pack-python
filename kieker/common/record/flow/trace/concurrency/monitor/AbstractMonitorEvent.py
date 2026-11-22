# since 1.8
# author Jan Waller

from kieker.common.record.flow.trace.AbstractTraceEvent import (
    AbstractTraceEvent,
)


class AbstractMonitorEvent (AbstractTraceEvent):
    def __init__(self, timestamp, trace_id, order_index, lock_id):
        super().__init__(timestamp, trace_id, order_index)
        self.lock_id = lock_id

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_int(self.lock_id) 

