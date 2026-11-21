# -*- coding: utf-8 -*-
# version 1.6
# author Jan Waller

from kieker.common.record.flow.IFlowRecord import IFlowRecord

class IExceptionRecord (IFlowRecord):
	def __init__(self, cause):	
		self.cause = (self.CAUSE
			if cause is None 
			else cause)
