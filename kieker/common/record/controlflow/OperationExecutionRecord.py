# version 0.91
# author Andre van Hoorn, Jan Waller


class OperationExecutionRecord:
	NO_HOSTNAME = "<default-host>"
	NO_SESSION_ID = "<no-session-id>"
	NO_OPERATION_SIGNATURE = "noOperation"
	NO_TRACE_ID = -1
	NO_TIMESTAMP = -1
	NO_EOI_ESS = -1
	def __init__(self, operation_signature, session_id, trace_id, tin, tout, hostname, eoi, ess):
		self.operation_signature = (self.NO_OPERATION_SIGNATURE
			if operation_signature is None 
			else operation_signature)
		self.session_id = (self.NO_SESSION_ID
			if session_id is None 
			else session_id)
		self.trace_id = trace_id
		self.tin = tin
		self.tout = tout
		self.hostname = (self.NO_HOSTNAME
			if hostname is None 
			else hostname)
		self.eoi = eoi
		self.ess = ess

	def serialize(self, serializer):
		serializer.put_string(self.operation_signature)
		serializer.put_string(self.session_id)
		serializer.put_long(self.trace_id)
		serializer.put_long(self.tin)
		serializer.put_long(self.tout)
		serializer.put_string(self.hostname)
		serializer.put_int(self.eoi)
		serializer.put_int(self.ess) 
	
	
