# -*- coding: utf-8 -*-
import threading
import random
import sys


threadLocal = threading.local()
lock = threading.Lock()


class TraceRegistry:
    def __init__(self):
        self.next_order_id = 0
        self.unique_id = random.randrange(sys.maxint)
        self.tracemetadata=None
    
