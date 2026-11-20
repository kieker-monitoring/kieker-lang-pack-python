class AfterOperationFailedEvent (AfterOperationEvent, IExceptionRecord
) :
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, cause):	
		cause = (self.CAUSE
				      if cause is None 
				      else cause)

	def serialize(self, serializer):
		serializer.put_string(self.cause) 
	
	
