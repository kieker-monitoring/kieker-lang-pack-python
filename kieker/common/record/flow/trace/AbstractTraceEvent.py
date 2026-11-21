# version 1.5
# author Jan Waller

from kieker.common.record.flow.AbstractEvent import AbstractEvent
from kieker.common.record.flow.ITraceRecord import ITraceRecord


class AbstractTraceEvent (AbstractEvent, ITraceRecord):
	def __init__(self, timestamp, trace_id, order_index):
		super().__init__(timestamp)
		self.trace_id = trace_id
		self.order_index = order_index

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_long(self.trace_id)
		serializer.put_int(self.order_index) 
	
	
