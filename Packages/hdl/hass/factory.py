from .const import DEFAULT_HOST, DEFAULT_PORT
from .hass import HassComms
from .device import HassDevice

class HassFactory:
    def __init__(self, token: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
        self.hass = HassComms(host=host, port=port, token=token)
        
    def devices(self) -> list[HassDevice]:
        """Get all HA devices"""
        # TODO: get all entity IDs from HA server
        
        # TODO: get all the drivers using self.device()
        pass
    
    def device(self, entity_id: str) -> HassDevice:
        """Get a HA device by entity ID"""
        # TODO: determine the type of the device by entity ID
        
        # TODO: construct HassDevice subclass object based on the device type
        pass
        