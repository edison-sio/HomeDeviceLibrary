from .ha_device import HaRequest, HaDevice, HaService
from base_device.base_light import BaseLight

class HaLight(HaDevice, BaseLight):
    """This class provides interface to control homeassistant light"""
    def __init__(self, 
                 url: str,
                 token: str,
                 entity_id: str,
                 ) -> None:
        super().__init__(url=url, token=token)
        self._entity_id = entity_id
        
    @property
    def entity_id(self) -> str:
        self._entity_id
        
    def set_on(self) -> bool:
        req = HaRequest(service=HaService.LIGHT_ON, data={"state": "on"})
        
        res = self.send_request_and_wait_response(req=req)
        
        if res:
            return True
        return False

    def set_off(self) -> bool:
        req = HaRequest(service=HaService.LIGHT_OFF, data={"state": "off"})
        
        res = self.send_request_and_wait_response(req=req)
        
        if res:
            return True
        return False
    
    def set_brightness(self, brightness: float):
        return super().set_brightness(brightness)        