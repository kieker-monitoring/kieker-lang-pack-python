# -*- coding: utf-8 -*-
# version 1.5
# author Andre van Hoorn, Holger Knoche, Jan Waller

from kieker.common.record.flow.trace.operation.AbstractOperationEvent import AbstractOperationEvent
from kieker.common.record.flow.ICallRecord import ICallRecord

class CallOperationEvent (AbstractOperationEvent, ICallRecord):
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, callee_operation_signature, callee_class_signature):
		super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature)
		self.callee_operation_signature = (self.CALLEE_OPERATION_SIGNATURE
				      if callee_operation_signature is None 
				      else callee_operation_signature)
		self.callee_class_signature = (self.CALLEE_CLASS_SIGNATURE
				      if callee_class_signature is None 
				      else callee_class_signature)

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.callee_operation_signature)
		serializer.put_string(self.callee_class_signature) 
	
	
