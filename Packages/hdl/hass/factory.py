from hdl.hass.const import (
    DEFAULT_HOST,
    DEFAULT_PORT,
    HassDomain,
)
from hdl.hass.hass import HassComms
from hdl.hass.device import HassDevice
from hdl.hass.light import HassLight
from hdl.hass.climate import HassClimate

class HassFactory:
    def __init__(self, token: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
        self.hass = HassComms(host=host, port=port, token=token)

        self._devices = {}
        
    def get_devices(self) -> dict[str, HassDevice]:
        """Get all HA devices"""

        # construct light driver
        entity_ids = self.hass.get_entity_ids(domain=HassDomain.LIGHT)

        for id in entity_ids:
            light = HassLight(entity_id=id, hass=self.hass)
            self._devices[id] = light

        # construct climate driver
        entity_ids = self.hass.get_entity_ids(domain=HassDomain.CLIMATE)
        for id in entity_ids:
            climate = HassClimate(entity_id=id, hass=self.hass)
            self._devices[id] = climate
        
        entity_ids = self.hass.get_entity_ids(domain=HassDomain.INPUT_BOOLEAN)
        
        
        return self._devices
    
    def get_device(self, entity_id: str) -> HassDevice:
        """Get a HA device by entity ID"""
        if entity_id not in self._devices.keys():
            raise KeyError(f"Unknown entity ID: {entity_id}")
        
        return self._devices[entity_id]
        