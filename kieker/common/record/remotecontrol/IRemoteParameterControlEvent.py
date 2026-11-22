# since 2.0.4
# author Generic Kieker

from kieker.common.record.remotecontrol.IRemoteControlEvent import (
    IRemoteControlEvent,
)


class IRemoteParameterControlEvent (IRemoteControlEvent):
    def __init__(self, pattern, name, values):	
        self.pattern = (""
            if pattern is None 
            else pattern)
        self.name = (""
            if name is None 
            else name)
        self.values = values
