from .device import HassDevice
from base_device.base_light import BaseLight
from .const import HassLightState
from .hass import HassComms

Color = tuple[float, float, float]
Temperature = float

class HassLight(HassDevice, BaseLight):
    """This class provides interface to control homeassistant light"""
    def __init__(self, 
                 name: str,
                 entity_id: str,
                 hass: HassComms,
                 ) -> None:
        super().__init__(name=name, entity_id=entity_id, hass=hass)
        
        self.brightness = 0

    
    
    def set_on(self) -> bool:
        res = self.set_state(HassLightState.ON)
        
        return True

    def set_off(self) -> bool:
        res = self.set_state(HassLightState.OFF)
        
        return True
    
    def set_color(self, color: Color) -> bool:
        
        return True
    
    def set_temperature(self, temp: Temperature) -> bool:
        
        return True
        
    
    def set_brightness(self, brightness: float):
        return super().set_brightness(brightness)        