# version 1.2
# author Andre van Hoorn, Jan Waller


class BranchingRecord:
	def __init__(self, timestamp, branch_id, branching_outcome):
		self.timestamp = timestamp
		self.branch_id = branch_id
		self.branching_outcome = branching_outcome

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_int(self.branch_id)
		serializer.put_int(self.branching_outcome) 
	
	
