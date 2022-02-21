# -*- coding: utf-8 -*-
import threading

#from socket import *
from monitoring.record import TraceMetadata


lock = threading.Lock()
thread_local = threading.local()



class _PointTrace:

    def __init__(self, trace_id, order_id):
        self.trace_id = trace_id
        self.order_id = order_id


class TraceRegistry:

    def __init__(self):
        self.next_order_id = 0
        self.next_trace_id = 0
        self.tracemetadata=None
        self.parent_trace = {}

    def get_trace(self):
        if not hasattr(thread_local, 'trace'):
            thread_local.trace = None
        return thread_local.trace

    def get_new_id(self):
        with lock:
            #  THIS IS A WEIRD WAY  TO INCREMENT
            # BUT FOR SOME REASON THE INCREMENTATION HAPPENS ONLY ONCE
            # IF WE DO IT NORMAL WAY. 
            tmp = self.next_trace_id
            self.next_trace_id = tmp + 1
            result = self.next_trace_id
        return 0 | result

    def get_and_remove_parent_trace_id(self, thread):
        lock.acquire()
        pass
        lock.release()

    def register_trace(self):
        # TODO Enclosingtaces and stuff
        thread = threading.current_thread()
        trace_point = None
        trace_id = self.get_new_id()
        parent_trace_id = 0
        parent_order_id = 0

        if trace_point is not None:
            parent_trace_id = trace_point.trace_id
            parent_order_id = trace_point.order_id
        else:
            parent_trace_id = trace_id
            parent_order_id = -1

        meta_record = TraceMetadata(trace_id,
                                    thread.ident,
                                    None,
                                    None,
                                    parent_trace_id,
                                    parent_order_id)
        thread_local.trace = meta_record
        return meta_record

    def unregister_trace(self):
        thread_local.trace = None
