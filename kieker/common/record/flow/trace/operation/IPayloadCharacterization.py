class IPayloadCharacterization:
	def __init__ (self):
		self.parameters
		values
		requestType = None
	@parameters.setter
	def parameters(self, value):
		if value.isinstance(string):
			self.parameters = value 
		else:
			raise Exception(f"Property parameters has type string but
					        a parameter with  type {value.type} was specified")
	
	@values.setter
	def values(self, value):
		if value.isinstance(string):
			self.values = value 
		else:
			raise Exception(f"Property values has type string but
					        a parameter with  type {value.type} was specified")
	
	@requestType.setter
	def requestType(self, value):
		if value.isinstance(int):
			self.requestType = value 
		else:
			raise Exception(f"Property requestType has type int but
					        a parameter with  type {value.type} was specified")
