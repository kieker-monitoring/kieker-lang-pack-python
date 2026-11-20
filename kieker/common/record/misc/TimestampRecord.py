class TimestampRecord :
	def __init__(self, timestamp):	
		timestamp = timestamp

	def serialize(self, serializer):
		serializer.put_long(self.timestamp) 
	
	
