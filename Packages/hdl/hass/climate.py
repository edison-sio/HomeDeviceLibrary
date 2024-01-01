from hdl.hass.const import (
    HassService,
    HassDomain,
)
from hdl.hass.hass import HassComms
from hdl.hass.device import HassDevice
from hdl.base_device.base_climate import BaseClimate
import enum

class ClimateMode(enum.Enum):
    """Climate mode"""
    FAN_ONLY = "fan_only"
    COOL = "cool"
    HEAT = "heat"
    DRY = "dry"


class HassClimate(HassDevice, BaseClimate):
    def __init__(self, entity_id: str, hass: HassComms) -> None:
        super().__init__(entity_id=entity_id, hass=hass)

        self._max_temp = None
        self._min_temp = None
        self._mode = None
    
    def turn_on(self) -> bool:
        """Turn on device"""
        data = {
            "entity_id": self.entity_id
        }
        res = self.hass.call_service(
            domain=HassDomain.CLIMATE,
            service=HassService.TURN_ON,
            data=data
        )

        return res.ok()

    def turn_off(self) -> bool:
        """Turn off device"""
        data = {
            "entity_id": self.entity_id
        }
        res = self.hass.call_service(
            domain=HassDomain.CLIMATE,
            service=HassService.TURN_OFF,
            data=data
        )

        return res.ok()

    def set_temperature(self, temperature: int) -> bool:
        """Set temperature"""
        data = {
            "entity_id": self.entity_id,
            "temperature": temperature
        }
        res = self.hass.call_service(
            domain=HassDomain.CLIMATE,
            service=HassService.SET_TEMPERATURE,
            data=data
        )

        return res.ok()
    
    # def set_mode(self, mode: ClimateMode) -> bool:
    #     """Set mode"""
    #     data = {
    #         "entity_id": self.entity_id
    #     }
    #     if mode == ClimateMode.
    #     res = self.hass.call_service(
    #         domain=HassDomain.CLIMATE,
    #         service=HassService.SET_
    #     )