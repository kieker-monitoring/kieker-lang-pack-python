class AbstractEvent (IEventRecord) :
	def __init__(self, timestamp):
		self.timestamp = timestamp

	def serialize(self, serializer):
		serializer.put_long(self.timestamp) 
	
	
