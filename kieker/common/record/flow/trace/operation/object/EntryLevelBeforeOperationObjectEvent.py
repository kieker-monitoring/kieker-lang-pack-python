class EntryLevelBeforeOperationObjectEvent (BeforeOperationObjectEvent, IPayloadCharacterization
) :
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id, parameters, values, request_type):	
		parameters = parameters
		values = values
		request_type = request_type

	def serialize(self, serializer):
		serializer.put_string(self.parameters)
		serializer.put_string(self.values)
		serializer.put_int(self.request_type) 
	
	
