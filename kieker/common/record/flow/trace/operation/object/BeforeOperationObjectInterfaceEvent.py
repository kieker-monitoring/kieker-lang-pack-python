# since 1.10
# author Florian Fittkau

from kieker.common.record.flow.IInterfaceRecord import IInterfaceRecord
from kieker.common.record.flow.trace.operation.object.BeforeOperationObjectEvent import (
    BeforeOperationObjectEvent,
)


class BeforeOperationObjectInterfaceEvent (BeforeOperationObjectEvent, IInterfaceRecord):
    def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id, interface):
        super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, object_id)
        self.interface = (""
            if interface is None
            else interface)

    def serialize(self, serializer):
        super().serialize(serializer)
        serializer.put_string(self.interface)

