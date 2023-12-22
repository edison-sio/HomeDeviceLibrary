import requests
from typing import Any
import enum
from .const import HassEndpoint, HassDeviceState
from .hass import HassComms

# class HaRequest(requests.Request):
#     def __init__(self, base_url: str, endpoint: HaEndpoint | str, data: dict[str, str]) -> None:
#         self.base_url = base_url
#         self.endpoint = endpoint
#         self.data = data
    
#     @property
#     def url(self) -> str:            
#         return f"{self.base_url}{self.endpoint}"
    

# class HaResponse(requests.Response):
#     def __init__(self, data: dict[str, str] | None = None):
#         self._data = data



class HassDevice:
    """Home Assistant Device"""
    def __init__(self, name: str, entity_id: str, hass: HassComms) -> None:
        self.hass = hass
        self.entity_id = entity_id
    
    def get_state(self) -> dict[str, str]:
        """Get device state"""
        endpoint = str(HassEndpoint.DEVICE_STATE).format(entity_id=self.entity_id)
        res = self.hass.get(
            endpoint=endpoint,
        )
        
        return res.json()
    
    def set_state(self, state: HassDeviceState | str) -> dict[str, str]:
        """Set device state"""
        data = {
            "state": f"{state}"
        }
        endpoint = str(HassEndpoint.DEVICE_STATE).format(entity_id=self.entity_id)
        res = self.hass.post(
            endpoint=endpoint,
            data=data
        )
        
        return res.json()