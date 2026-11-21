# -*- coding: utf-8 -*-
# version 1.6
# author Jan Waller

from kieker.common.record.flow.IFlowRecord import IFlowRecord
from kieker.common.record.flow.IClassSignature import IClassSignature

class IObjectRecord (IFlowRecord, IClassSignature):
	def __init__(self, class_signature, object_id):	
		self.class_signature = (self.CLASS_SIGNATURE
		      if class_signature is None 
		      else class_signature)
		self.object_id = object_id
