# -*- coding: utf-8 -*-
# version 2.0.0
# author Reiner Jung


class ISessionEvent:
	def __init__(self, hostname, session_id):	
		self.hostname = (""
			if hostname is None 
			else hostname)
		self.session_id = (""
			if session_id is None 
			else session_id)
