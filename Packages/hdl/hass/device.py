import requests
from typing import Any
import enum
import abc
from hdl.hass.const import (
    HassEndpoint,
    HassDeviceState,
    HassService,
    HassDomain
)
from hdl.hass.hass import HassComms
from typing import Any

class HassState:
    def __init__(self, state: dict[str, Any]) -> None:
        self._state = state
    
    def __str__(self) -> str:
        return str(self.json())

    def json(self) -> dict[str, Any]:
        return self._state

class HassDevice:
    """Home Assistant Device"""
    def __init__(self, entity_id: str, hass: HassComms) -> None:
        self.hass = hass
        self.entity_id = entity_id
    
    def get_state(self) -> HassState:
        """Get device state"""
        endpoint = str(HassEndpoint.DEVICE_STATE).format(entity_id=self.entity_id)
        res = self.hass.get(
            endpoint=endpoint,
        )
        
        state = res.json()
        return HassState(state)

