# version 2.0.0
# author Reiner Jung


class OperationCallEvent:
	def __init__(self, source_component, source_operation, target_component, target_operation):
		self.source_component = (""
			if source_component is None 
			else source_component)
		self.source_operation = (""
			if source_operation is None 
			else source_operation)
		self.target_component = (""
			if target_component is None 
			else target_component)
		self.target_operation = (""
			if target_operation is None 
			else target_operation)

	def serialize(self, serializer):
		serializer.put_string(self.source_component)
		serializer.put_string(self.source_operation)
		serializer.put_string(self.target_component)
		serializer.put_string(self.target_operation) 
	
	
