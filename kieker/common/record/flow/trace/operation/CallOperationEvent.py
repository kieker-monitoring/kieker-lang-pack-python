class CallOperationEvent (AbstractOperationEvent, ICallRecord
) :
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature):	
		callee_operation_signature = (self.CALLEE_OPERATION_SIGNATURE
				      if callee_operation_signature is None 
				      else callee_operation_signature)
		callee_class_signature = (self.CALLEE_CLASS_SIGNATURE
				      if callee_class_signature is None 
				      else callee_class_signature)

	def serialize(self, serializer):
		serializer.put_string(self.callee_operation_signature)
		serializer.put_string(self.callee_class_signature) 
	
	
