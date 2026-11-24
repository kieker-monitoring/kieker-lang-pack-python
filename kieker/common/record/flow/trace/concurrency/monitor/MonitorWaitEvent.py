# since 1.8
# author Jan Waller

from kieker.common.record.flow.trace.concurrency.monitor.AbstractMonitorEvent import (
    AbstractMonitorEvent,
)


class MonitorWaitEvent (AbstractMonitorEvent):
    def __init__(self, timestamp, trace_id, order_index, lock_id):
        super().__init__(timestamp, trace_id, order_index, lock_id)

    def serialize(self, serializer):
        super().serialize(serializer)

