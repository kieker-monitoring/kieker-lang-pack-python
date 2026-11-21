# -*- coding: utf-8 -*-
# version 1.14
# author Marc Adolf


class IRemoteControlEvent:
	def __init__(self, pattern):	
		self.pattern = (""
			if pattern is None 
			else pattern)
