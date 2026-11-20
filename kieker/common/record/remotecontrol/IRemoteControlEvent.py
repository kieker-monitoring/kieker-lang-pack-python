class IRemoteControlEvent:
	def __init__ (self):
		self.pattern = None
	@pattern.setter
	def pattern(self, value):
		if value.isinstance(string):
			self.pattern = value 
		else:
			raise Exception(f"Property pattern has type string but
					        a parameter with  type {value.type} was specified")
