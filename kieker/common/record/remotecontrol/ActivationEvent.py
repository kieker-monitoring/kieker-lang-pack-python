class ActivationEvent :
	def __init__(self, pattern):	
		pattern = (""
				      if pattern is None 
				      else pattern)

	def serialize(self, serializer):
		serializer.put_string(self.pattern) 
	
	
