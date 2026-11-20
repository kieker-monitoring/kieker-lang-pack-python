class ThreadMetaData :
	def __init__(self, hostname, thread_id):	
		hostname = (""
				      if hostname is None 
				      else hostname)
		thread_id = thread_id

	def serialize(self, serializer):
		serializer.put_string(self.hostname)
		serializer.put_long(self.thread_id) 
	
	
