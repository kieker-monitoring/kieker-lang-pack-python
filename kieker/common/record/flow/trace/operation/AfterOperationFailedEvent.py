# -*- coding: utf-8 -*-
# version 1.5
# author Jan Waller

from kieker.common.record.flow.trace.operation.AfterOperationEvent import AfterOperationEvent
from kieker.common.record.flow.IExceptionRecord import IExceptionRecord

class AfterOperationFailedEvent (AfterOperationEvent, IExceptionRecord):
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, cause):
		super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature)
		self.cause = (self.CAUSE
				      if cause is None 
				      else cause)

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.cause) 
	
	
