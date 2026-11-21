# -*- coding: utf-8 -*-
# version 1.14
# author Felix Eichhorst


class BeforeSentRemoteEvent:
	def __init__(self, timestamp, trace_id, order_index, technology):
		self.timestamp = timestamp
		self.trace_id = trace_id
		self.order_index = order_index
		self.technology = (self.TECHNOLOGY
			if technology is None 
			else technology)

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_long(self.trace_id)
		serializer.put_int(self.order_index)
		serializer.put_string(self.technology) 
	
	
