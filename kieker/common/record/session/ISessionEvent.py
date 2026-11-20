class ISessionEvent:
	def __init__ (self):
		self.hostname
		sessionId = None
	@hostname.setter
	def hostname(self, value):
		if value.isinstance(string):
			self.hostname = value 
		else:
			raise Exception(f"Property hostname has type string but
					        a parameter with  type {value.type} was specified")
	
	@sessionId.setter
	def sessionId(self, value):
		if value.isinstance(string):
			self.sessionId = value 
		else:
			raise Exception(f"Property sessionId has type string but
					        a parameter with  type {value.type} was specified")
