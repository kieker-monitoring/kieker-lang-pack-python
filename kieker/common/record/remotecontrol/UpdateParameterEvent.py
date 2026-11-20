class UpdateParameterEvent :
	def __init__(self, pattern, name, values):	
		pattern = (""
				      if pattern is None 
				      else pattern)
		name = (""
				      if name is None 
				      else name)
		values = values

	def serialize(self, serializer):
		serializer.put_string(self.pattern)
		serializer.put_string(self.name)
		serializer.put_string(self.values) 
	
	
