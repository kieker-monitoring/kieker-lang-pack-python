class SessionEndEvent :
	def __init__(self, timestamp, hostname, session_id):	
		timestamp = timestamp
		hostname = (""
				      if hostname is None 
				      else hostname)
		session_id = (""
				      if session_id is None 
				      else session_id)

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.hostname)
		serializer.put_string(self.session_id) 
	
	
