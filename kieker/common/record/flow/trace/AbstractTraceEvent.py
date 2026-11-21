# -*- coding: utf-8 -*-
# version 1.5
# author Jan Waller

from kieker.common.record.flow.AbstractEvent import AbstractEvent
from kieker.common.record.flow.ITraceRecord import ITraceRecord

class AbstractTraceEvent (AbstractEvent, ITraceRecord):
	def __init__(self, timestamp, trace_id, order_index):
		super().__init__(timestamp)
		MISSING CLASSIFIER for traceId
		self.order_index = order_index

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_Event.createTypeName missing classifier(self.trace_id)
		serializer.put_int(self.order_index) 
	
	
