# since 1.8
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.trace.concurrency.monitor.AbstractMonitorEvent import (
    AbstractMonitorEvent,
)


class MonitorNotifyAllEvent (AbstractMonitorEvent):
    def __init__(self, timestamp, trace_id, order_index, lock_id):
        super().__init__(timestamp, trace_id, order_index, lock_id)

    def serialize(self, serializer):
        super().serialize(serializer)

