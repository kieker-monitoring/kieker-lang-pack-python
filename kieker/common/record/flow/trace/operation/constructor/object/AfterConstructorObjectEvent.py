class AfterConstructorObjectEvent (AfterConstructorEvent, IObjectRecord
) :
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id):	
		object_id = object_id

	def serialize(self, serializer):
		serializer.put_int(self.object_id) 
	
	
