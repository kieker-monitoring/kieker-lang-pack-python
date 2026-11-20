class IParameterValueEvent (IRemoteControlEvent
):
	def __init__ (self):
		self.name
		value = None
	@name.setter
	def name(self, value):
		if value.isinstance(string):
			self.name = value 
		else:
			raise Exception(f"Property name has type string but
					        a parameter with  type {value.type} was specified")
	
	@value.setter
	def value(self, value):
		if value.isinstance(string):
			self.value = value 
		else:
			raise Exception(f"Property value has type string but
					        a parameter with  type {value.type} was specified")
