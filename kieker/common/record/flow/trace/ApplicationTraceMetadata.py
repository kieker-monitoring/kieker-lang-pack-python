class ApplicationTraceMetadata (TraceMetadata, ) :
	NO_APPLICATION_NAME = "<no-application-name>"
	def __init__(self, trace_id, thread_id, session_id, hostname, parent_trace_id, parent_order_id, application_name):	
		application_name = (self.NO_APPLICATION_NAME
				      if application_name is None 
				      else application_name)

	def serialize(self, serializer):
		serializer.put_string(self.application_name) 
	
	
