class BeforeOperationObjectInterfaceEvent (BeforeOperationObjectEvent, IInterfaceRecord
) :
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id, interface):	
		interface = (""
				      if interface is None 
				      else interface)

	def serialize(self, serializer):
		serializer.put_string(self.interface) 
	
	
