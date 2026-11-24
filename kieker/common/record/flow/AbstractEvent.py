# since 1.5
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IEventRecord import IEventRecord


class AbstractEvent (IEventRecord):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)

