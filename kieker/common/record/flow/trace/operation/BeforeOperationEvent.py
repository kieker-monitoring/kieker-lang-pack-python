# -*- coding: utf-8 -*-
# version 1.5
# author Jan Waller

from kieker.common.record.flow.trace.operation.AbstractOperationEvent import AbstractOperationEvent

class BeforeOperationEvent (AbstractOperationEvent):
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature):
		super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature)

	def serialize(self, serializer):
		super().serialize(serializer)
	
	
