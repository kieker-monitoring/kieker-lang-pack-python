class RemoveParameterValueEvent :
	def __init__(self, pattern, name, value):	
		pattern = (""
				      if pattern is None 
				      else pattern)
		name = (""
				      if name is None 
				      else name)
		value = (""
				      if value is None 
				      else value)

	def serialize(self, serializer):
		serializer.put_string(self.pattern)
		serializer.put_string(self.name)
		serializer.put_string(self.value) 
	
	
