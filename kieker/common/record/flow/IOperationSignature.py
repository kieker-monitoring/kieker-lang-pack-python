# version 1.10
# author Reiner Jung


class IOperationSignature:
	def __init__(self, operation_signature):	
		self.operation_signature = (self.OPERATION_SIGNATURE
			if operation_signature is None 
			else operation_signature)
