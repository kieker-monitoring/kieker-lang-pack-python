# since 1.6
# author Jan Waller

from kieker.common.record.flow.ICallRecord import ICallRecord
from kieker.common.record.flow.IObjectRecord import IObjectRecord


class ICallObjectRecord (ICallRecord, IObjectRecord):
    def __init__(self, operation_signature, class_signature, callee_operation_signature, callee_class_signature, object_id, callee_object_id):	
        self.operation_signature = (self.OPERATION_SIGNATURE
            if operation_signature is None 
            else operation_signature)
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None 
            else class_signature)
        self.caller_operation_signature = self.operation_signature
        self.caller_class_signature = self.class_signature
        self.callee_operation_signature = (self.CALLEE_OPERATION_SIGNATURE
            if callee_operation_signature is None 
            else callee_operation_signature)
        self.callee_class_signature = (self.CALLEE_CLASS_SIGNATURE
            if callee_class_signature is None 
            else callee_class_signature)
        self.object_id = object_id
        self.caller_object_id = self.object_id
        self.callee_object_id = callee_object_id
