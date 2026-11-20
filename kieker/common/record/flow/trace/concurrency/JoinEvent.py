class JoinEvent (AbstractTraceEvent, ) :
	def __init__(self, timestamp, trace_id, order_index, joined_trace_id):	
		joined_trace_id = joined_trace_id

	def serialize(self, serializer):
		serializer.put_long(self.joined_trace_id) 
	
	
