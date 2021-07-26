# -*- coding: utf-8 -*-
import time
import calendar

class TimeStamp:
    
    def get_time(self):
        timestamp = calendar.timegm(time.gmtime())
        return time.ctime(timestamp)