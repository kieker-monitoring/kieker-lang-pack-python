# -*- coding: utf-8 -*-
# version 1.10
# author Nils Christian Ehmke

from kieker.common.record.jvm.AbstractJVMRecord import AbstractJVMRecord

class CompilationRecord (AbstractJVMRecord):
	def __init__(self, timestamp, hostname, vm_name, jit_compiler_name, total_compilation_time_ms):
		super().__init__(timestamp, hostname, vm_name)
		self.jit_compiler_name = (""
				      if jit_compiler_name is None 
				      else jit_compiler_name)
		self.total_compilation_time_ms = total_compilation_time_ms

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.jit_compiler_name)
		serializer.put_long(self.total_compilation_time_ms) 
	
	
