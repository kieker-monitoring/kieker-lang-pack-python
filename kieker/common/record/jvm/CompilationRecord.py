class CompilationRecord (AbstractJVMRecord, ) :
	def __init__(self, timestamp, hostname, vm_name, jit_compiler_name, total_compilation_time_ms):	
		jit_compiler_name = (""
				      if jit_compiler_name is None 
				      else jit_compiler_name)
		total_compilation_time_ms = total_compilation_time_ms

	def serialize(self, serializer):
		serializer.put_string(self.jit_compiler_name)
		serializer.put_long(self.total_compilation_time_ms) 
	
	
