# since 1.12
# author Teerat Pitakrat



class LoadAverageRecord:
    def __init__(self, timestamp, hostname, one_min_load_average, five_min_load_average, fifteen_min_load_average):
        self.timestamp = timestamp
        self.hostname = (self.HOSTNAME
            if hostname is None
            else hostname)
        self.one_min_load_average = one_min_load_average
        self.five_min_load_average = five_min_load_average
        self.fifteen_min_load_average = fifteen_min_load_average

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)
        serializer.put_string(self.hostname)
        serializer.put_double(self.one_min_load_average)
        serializer.put_double(self.five_min_load_average)
        serializer.put_double(self.fifteen_min_load_average)

