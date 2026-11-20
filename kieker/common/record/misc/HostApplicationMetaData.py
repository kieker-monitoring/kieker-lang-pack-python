class HostApplicationMetaData :
	def __init__(self, system_name, ip_address, hostname, application_name):	
		system_name = (""
				      if system_name is None 
				      else system_name)
		ip_address = (""
				      if ip_address is None 
				      else ip_address)
		hostname = (""
				      if hostname is None 
				      else hostname)
		application_name = (""
				      if application_name is None 
				      else application_name)

	def serialize(self, serializer):
		serializer.put_string(self.system_name)
		serializer.put_string(self.ip_address)
		serializer.put_string(self.hostname)
		serializer.put_string(self.application_name) 
	
	
