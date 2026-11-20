class CallConstructorObjectEvent (CallConstructorEvent, ICallObjectRecord
) :
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature, object_id, callee_object_id):	
		object_id = object_id
		callee_object_id = callee_object_id

	def serialize(self, serializer):
		serializer.put_int(self.object_id)
		serializer.put_int(self.callee_object_id) 
	
	
