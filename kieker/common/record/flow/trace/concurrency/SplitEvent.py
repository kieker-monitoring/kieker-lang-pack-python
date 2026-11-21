# version 1.5
# author Jan Waller

from kieker.common.record.flow.trace.AbstractTraceEvent import AbstractTraceEvent


class SplitEvent (AbstractTraceEvent):
	def __init__(self, timestamp, trace_id, order_index):
		super().__init__(timestamp, trace_id, order_index)

	def serialize(self, serializer):
		super().serialize(serializer)
	
	
