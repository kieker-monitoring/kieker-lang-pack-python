# version 1.6
# author Jan Waller

from kieker.common.record.flow.IConstructorRecord import IConstructorRecord
from kieker.common.record.flow.trace.operation.AfterOperationFailedEvent import (
	AfterOperationFailedEvent,
)


class AfterConstructorFailedEvent (AfterOperationFailedEvent, IConstructorRecord):
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, cause):
		super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, cause)

	def serialize(self, serializer):
		super().serialize(serializer)
	
	
