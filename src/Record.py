# -*- coding: utf-8 -*-


class Serializer:

    def __init__(self, string_byte):
        self.string_byte = string_byte

    def put(self, value):
        self.string_byte.append(value+"; ")


class DummyRecord:

    def __init__(self, foo_parameter, bar_parameter):
        # self.serializer=serializer
        self.foo_parameter = foo_parameter
        self.bar_parameter = bar_parameter

    def serialize(self, serializer):
        serializer.put(self.foo_parameter)
        serializer.put(self.bar_parameter)


class OperationExecutionRecord:

    __NO_HOSTNAME__ = "<default-host>"
    __NO_SESSION_ID__ = "<no-session-id>"
    __NO_OPERATION_SIGNATURE__ = "noOperation"
    __NO_TRACE_ID__ = -1
    __NO_TIMESTAMP__ = -1
    __NO_EOI_ESS__ = -1
    __VALUES__ = ["operation_siganture", "session_id",
                  "trace_id", "tin", "tout", "hostname", "eoi", "ess"]

    def __init__(self, operation_signature, session_id,
                 trace_id, tin, tout, hostname, eoi, ess):
        self.operation_signature = (self.__NO_OPERATION_SIGNATURE__
                                    if operation_signature is None
                                    else operation_signature)
        self.session_id = (self.__NO_SESSION_ID__
                           if session_id is None
                           else operation_signature)
        self.trace_id = trace_id
        self.tin = tin
        self.tou = tout
        self.hostname = self.__NO_HOSTNAME__ if hostname is None else hostname
        self.eoi = eoi
        self.ess = ess
