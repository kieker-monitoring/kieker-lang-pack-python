# -*- coding: utf-8 -*-
# version 1.10
# author Florian Fittkau

from kieker.common.record.flow.trace.operation.constructor.object.BeforeConstructorObjectEvent import BeforeConstructorObjectEvent
from kieker.common.record.flow.IInterfaceRecord import IInterfaceRecord

class BeforeConstructorObjectInterfaceEvent (BeforeConstructorObjectEvent, IInterfaceRecord):
	def __init__(self, timestamp, trace_id, order_index, operation_signature, class_signature, object_id, interface):
		super().__init__(timestamp, trace_id, order_index, operation_signature, class_signature, object_id)
		self.interface = (""
			if interface is None 
			else interface)

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.interface) 
	
	
