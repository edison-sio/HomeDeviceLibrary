from hdl.hass.device import HassDevice
from hdl.base_device.base_light import BaseLight
from hdl.hass.const import (
    HassDeviceState,
    HassDomain,
    HassService,
)
from hdl.hass.hass import HassComms
import enum

Color = tuple[float, float, float]


Temperature = float
Brightness = float

class HassLightState(HassDeviceState):
    """Light state"""
    ON  = "on"
    OFF = "off"

class HassLight(HassDevice, BaseLight):
    """This class provides interface to control homeassistant light"""
    def __init__(self,
                 entity_id: str,
                 hass: HassComms,
                 ) -> None:
        super().__init__(entity_id=entity_id, hass=hass)


    def __str__(self) -> str:
        return f"<HassLight: {self.entity_id}>"
    
    def turn_on(self) -> bool:
        """Turn on the light"""
        data = {
            "entity_id": self.entity_id
        }
        res = self.hass.call_service(
            domain=HassDomain.LIGHT,
            service=HassService.TURN_ON,
            data=data
        )
        
        if res.status_code == 200:
            return True
        return False

    def turn_off(self) -> bool:
        """Turn off the light"""
        data = {
            "entity_id": self.entity_id
        }
        res = self.hass.call_service(
            domain=HassDomain.LIGHT,
            service=HassService.TURN_OFF,
            data=data
        )
        
        if res.status_code == 200:
            return True
        return False
    
    def set_color(self, color: Color) -> bool:
        """Set light color"""
        data = {
            "entity_id": self.entity_id,
            "rgb_color": list(color)
        }
        res = self.hass.call_service(
            domain=HassDomain.LIGHT,
            service=HassService.TURN_ON,
            data=data
        )

        if res.status_code == 200:
            return True
        
        return False
    
    def set_temperature(self, temp: Temperature) -> bool:
        
        return True
        
    
    def set_brightness(self, brightness: float) -> bool:
        if brightness <= 1 or brightness > 255:
            return False

        data = {
            "entity_id": self.entity_id,
            "brightness": brightness
        }
        res = self.hass.call_service(
            domain=HassDomain.LIGHT,
            service=HassService.TURN_ON,
            data=data
        )

        if res.status_code == 200:
            return True
        return False
    
    def get_state(self) -> HassLightState:
        """Get light state"""
        res = super().get_state()

        return res