class ConstructionEvent (AbstractTraceEvent, ) :
	def __init__(self, timestamp, trace_id, order_index, class_signature, object_id):	
		class_signature = (self.CLASS_SIGNATURE
				      if class_signature is None 
				      else class_signature)
		object_id = object_id

	def serialize(self, serializer):
		serializer.put_string(self.class_signature)
		serializer.put_int(self.object_id) 
	
	
