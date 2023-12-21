import broadlink
import time
from typing import Any
import logging

class BroadlinkRemote:
    def __init__(self, ip: str, log: Any = print) -> None:
        self._ip = ip
        self._device = broadlink.hello(host=ip)
        if not self._device.auth():
            raise Exception()

        self.log = log
    
    def learn_ir(self, timeout: float = 10.) -> bytes:
        """Learn IR code"""
        self.log("Start learning IR code...")
        self.log("Waiting for input...")
        learned = self._start_and_wait_for_ir_code(timeout=timeout)
        
        if not learned:
            raise Exception("BroadlinkRemote.learn_ir: timeout")

        return learned
    
    def learn_rf(self, timeout: float = 10.) -> bytes:
        """Learn RF code"""
        ...
    
    def _start_and_wait_for_ir_code(self, timeout: float = 10.) -> bytes | None:
        """Start waiting for the IR code to be learned"""
        learned = None
        self._device.enter_learning()
        
        start = time.time()
        while learned is None:
            if time.time() - start > timeout:
                return None
            
            try:
                learned = self._device.check_data()
            except:
                learned = None
        
        return learned
    
    def _start_and_wait_for_rf_code(self, timeout: float = 10.) -> bytes | None:
        """Start waiting for the RF code to be learned"""
        ...