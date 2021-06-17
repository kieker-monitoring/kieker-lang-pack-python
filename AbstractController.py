# -*- coding: utf-8 -*-

# I HAVE NO IDEA WHAT I AM DOING

#/***************************************************************************
#* Copyright 2020 Kieker Project (http://kieker-monitoring.net)
#*
#* Licensed under the Apache License, Version 2.0 (the "License");
#* you may not use this file except in compliance with the License.
#* You may obtain a copy of the License at
#*
#*     http://www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software
#* distributed under the License is distributed on an "AS IS" BASIS,
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#* See the License for the specific language governing permissions and
#* limitations under the License.
#***************************************************************************/
import logging
import threading
class AbstractController :
    
    def __init__(self, domain, tcp_enabled, reader_thread, port, buffer_capacity,
               terminated):
        self.domain=domain
        self.tcp_enabled=tcp_enabled
        self.reader_function=reader_thread
        self.port=port
        self.buffer_capacity=buffer_capacity
        self.terminated=terminated
        self.logger=logging.getLogger('ControllerLogger')
        
    def initialize(self):
        if self.tcp_enabled==True :
            self.logger.info('Start Thread reader')
            self.threading.start()
    

    def cleanup(self):
        if self.tcp_enabled:
            self.logger.info('Terminate')
        