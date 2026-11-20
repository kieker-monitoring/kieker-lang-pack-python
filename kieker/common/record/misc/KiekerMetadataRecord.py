class KiekerMetadataRecord :
	NO_CONTROLLERNAME = "<no-controller-name>"
	NO_HOSTNAME = "<no-hostname>"
	NO_TIMESOURCE = "<no-timesource>"
	NO_TIMEUNIT = "NANOSECONDS"
	def __init__(self, version, controller_name, hostname, experiment_id, debug_mode, time_offset, time_unit, number_of_records):	
		version = (self.VERSION
				      if version is None 
				      else version)
		controller_name = (self.NO_CONTROLLERNAME
				      if controller_name is None 
				      else controller_name)
		hostname = (self.NO_HOSTNAME
				      if hostname is None 
				      else hostname)
		experiment_id = experiment_id
		debug_mode = debug_mode
		time_offset = time_offset
		time_unit = (self.NO_TIMEUNIT
				      if time_unit is None 
				      else time_unit)
		number_of_records = number_of_records

	def serialize(self, serializer):
		serializer.put_string(self.version)
		serializer.put_string(self.controller_name)
		serializer.put_string(self.hostname)
		serializer.put_int(self.experiment_id)
		serializer.put_boolean(self.debug_mode)
		serializer.put_long(self.time_offset)
		serializer.put_string(self.time_unit)
		serializer.put_long(self.number_of_records) 
	
	
