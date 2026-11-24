# since 1.13
# author Christian Wulf

# Modified by Natalie Kaufhold, 2026
from common.record.flow.thread.AbstractThreadBasedEvent import (
    AbstractThreadBasedEvent,
)


class AfterThreadBasedEvent (AbstractThreadBasedEvent):
    def __init__(self, timestamp, thread_id, order_index, operation_signature, class_signature):
        super().__init__(timestamp, thread_id, order_index, operation_signature, class_signature)

    def serialize(self, serializer):
        super().serialize(serializer)

