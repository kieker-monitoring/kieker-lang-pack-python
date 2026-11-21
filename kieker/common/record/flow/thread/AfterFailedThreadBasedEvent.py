# -*- coding: utf-8 -*-
# version 1.13
# author Christian Wulf

from kieker.common.record.flow.thread.AbstractThreadBasedEvent import AbstractThreadBasedEvent
from kieker.common.record.flow.IExceptionRecord import IExceptionRecord

class AfterFailedThreadBasedEvent (AbstractThreadBasedEvent, IExceptionRecord):
	def __init__(self, timestamp, thread_id, order_index, operation_signature, class_signature, cause):
		super().__init__(timestamp, thread_id, order_index, operation_signature, class_signature)
		self.cause = (self.CAUSE
				      if cause is None 
				      else cause)

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.cause) 
	
	
