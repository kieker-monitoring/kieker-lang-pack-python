# -*- coding: utf-8 -*-
# version 1.12
# author Teerat Pitakrat


class NetworkUtilizationRecord:
	def __init__(self, timestamp, hostname, interface_name, speed, tx_bytes_per_second, tx_carrier_per_second, tx_collisions_per_second, tx_dropped_per_second, tx_errors_per_second, tx_overruns_per_second, tx_packets_per_second, rx_bytes_per_second, rx_dropped_per_second, rx_errors_per_second, rx_frame_per_second, rx_overruns_per_second, rx_packets_per_second):
		self.timestamp = timestamp
		self.hostname = (self.HOSTNAME
			if hostname is None 
			else hostname)
		self.interface_name = (self.INTERFACE_NAME
			if interface_name is None 
			else interface_name)
		self.speed = speed
		self.tx_bytes_per_second = tx_bytes_per_second
		self.tx_carrier_per_second = tx_carrier_per_second
		self.tx_collisions_per_second = tx_collisions_per_second
		self.tx_dropped_per_second = tx_dropped_per_second
		self.tx_errors_per_second = tx_errors_per_second
		self.tx_overruns_per_second = tx_overruns_per_second
		self.tx_packets_per_second = tx_packets_per_second
		self.rx_bytes_per_second = rx_bytes_per_second
		self.rx_dropped_per_second = rx_dropped_per_second
		self.rx_errors_per_second = rx_errors_per_second
		self.rx_frame_per_second = rx_frame_per_second
		self.rx_overruns_per_second = rx_overruns_per_second
		self.rx_packets_per_second = rx_packets_per_second

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.hostname)
		serializer.put_string(self.interface_name)
		serializer.put_long(self.speed)
		serializer.put_double(self.tx_bytes_per_second)
		serializer.put_double(self.tx_carrier_per_second)
		serializer.put_double(self.tx_collisions_per_second)
		serializer.put_double(self.tx_dropped_per_second)
		serializer.put_double(self.tx_errors_per_second)
		serializer.put_double(self.tx_overruns_per_second)
		serializer.put_double(self.tx_packets_per_second)
		serializer.put_double(self.rx_bytes_per_second)
		serializer.put_double(self.rx_dropped_per_second)
		serializer.put_double(self.rx_errors_per_second)
		serializer.put_double(self.rx_frame_per_second)
		serializer.put_double(self.rx_overruns_per_second)
		serializer.put_double(self.rx_packets_per_second) 
	
	
