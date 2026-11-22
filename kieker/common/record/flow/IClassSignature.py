# since 1.10
# author Reiner Jung



class IClassSignature:
    def __init__(self, class_signature):	
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None 
            else class_signature)
