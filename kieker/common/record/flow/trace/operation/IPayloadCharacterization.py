# version 2.0.0
# author Reiner Jung


class IPayloadCharacterization:
	def __init__(self, parameters, values, request_type):	
		self.parameters = parameters
		self.values = values
		self.request_type = request_type
