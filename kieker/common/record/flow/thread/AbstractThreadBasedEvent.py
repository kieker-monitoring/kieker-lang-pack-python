# -*- coding: utf-8 -*-
# version 1.13
# author Christian Wulf

from kieker.common.record.flow.AbstractEvent import AbstractEvent
from kieker.common.record.flow.IThreadBasedRecord import IThreadBasedRecord
from kieker.common.record.flow.IOperationSignature import IOperationSignature
from kieker.common.record.flow.IClassSignature import IClassSignature

class AbstractThreadBasedEvent (AbstractEvent, IThreadBasedRecord, IOperationSignature, IClassSignature):
	def __init__(self, timestamp, thread_id, order_index, operation_signature, class_signature):
		super().__init__(timestamp)
		self.thread_id = thread_id
		self.order_index = order_index
		self.operation_signature = (self.OPERATION_SIGNATURE
				      if operation_signature is None 
				      else operation_signature)
		self.class_signature = (self.CLASS_SIGNATURE
				      if class_signature is None 
				      else class_signature)

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_long(self.thread_id)
		serializer.put_int(self.order_index)
		serializer.put_string(self.operation_signature)
		serializer.put_string(self.class_signature) 
	
	
