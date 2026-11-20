class IRemoteParameterControlEvent (IRemoteControlEvent
):
	def __init__ (self):
		self.name
		values = None
	@name.setter
	def name(self, value):
		if value.isinstance(string):
			self.name = value 
		else:
			raise Exception(f"Property name has type string but
					        a parameter with  type {value.type} was specified")
	
	@values.setter
	def values(self, value):
		if value.isinstance(string):
			self.values = value 
		else:
			raise Exception(f"Property values has type string but
					        a parameter with  type {value.type} was specified")
