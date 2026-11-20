class ResourceUtilizationRecord :
	def __init__(self, timestamp, hostname, resource_name, utilization):	
		timestamp = timestamp
		hostname = (self.HOSTNAME
				      if hostname is None 
				      else hostname)
		resource_name = (self.RESOURCE_NAME
				      if resource_name is None 
				      else resource_name)
		utilization = utilization

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.hostname)
		serializer.put_string(self.resource_name)
		serializer.put_double(self.utilization) 
	
	
