# version 2.0.0
# author Reiner Jung

from kieker.common.record.flow.trace.operation.IPayloadCharacterization import (
	IPayloadCharacterization,
)
from kieker.common.record.flow.trace.operation.object.BeforeOperationObjectEvent import (
	BeforeOperationObjectEvent,
)


class EntryLevelBeforeOperationObjectEvent (BeforeOperationObjectEvent, IPayloadCharacterization):
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id, parameters, values, request_type):
		super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, object_id)
		self.parameters = parameters
		self.values = values
		self.request_type = request_type

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.parameters)
		serializer.put_string(self.values)
		serializer.put_int(self.request_type) 
	
	
