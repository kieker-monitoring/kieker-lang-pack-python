# version 1.14
# author Christian Zirkelbach (czi@informatik.uni-kiel.de)

from kieker.common.record.flow.IClassSignature import IClassSignature
from kieker.common.record.flow.IEventRecord import IEventRecord
from kieker.common.record.flow.IFlowRecord import IFlowRecord
from kieker.common.record.flow.ITraceRecord import ITraceRecord


class AfterDatabaseEvent (IEventRecord, IFlowRecord, IClassSignature, ITraceRecord):
	def __init__(self, timestamp, class_signature, trace_id, order_index, return_type, return_value):
		self.timestamp = timestamp
		self.class_signature = (self.CLASS_SIGNATURE
			if class_signature is None 
			else class_signature)
		self.trace_id = trace_id
		self.order_index = order_index
		self.return_type = (""
			if return_type is None 
			else return_type)
		self.return_value = (""
			if return_value is None 
			else return_value)

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.class_signature)
		serializer.put_long(self.trace_id)
		serializer.put_int(self.order_index)
		serializer.put_string(self.return_type)
		serializer.put_string(self.return_value) 
	
	
