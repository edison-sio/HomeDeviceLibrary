import requests
from typing import Any
import enum

class HaEndpoint(enum.Enum):
    """This class stores Home Assistant API endpoints"""
    def __str__(self) -> str:
        return self.value

    LIGHT_TOGGLE = "/light/toggle"
    LIGHT_ON     = "/light/on"
    LIGHT_OFF    = "/light/off"

    SWITCH_TOGGLE = "/switch/toggle"
    SWITCH_ON     = "/switch/on"
    SWITCH_OFF    = "/swtich/off"
    ...


class HaRequest(requests.Request):
    def __init__(self, base_url: str, endpoint: HaEndpoint | str, data: dict[str, str]) -> None:
        self.base_url = base_url
        self.endpoint = endpoint
        self.data = data
    
    @property
    def url(self) -> str:            
        return f"{self.base_url}{self.endpoint}"
    

class HaResponse(requests.Response):
    def __init__(self, data: dict[str, str] | None = None):
        self._data = data

    @property
    def data(self) -> dict[str, str] | None:
        return self._data

class HaDevice:
    """Home Assistant Device"""
    def __init__(self, url: str, token: str) -> None:
        self._url = url
        self._token = token
    
    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }
    
    def send_request(self, endpoint: str, data: dict[str, str]) -> None:
        """Send a request to the HA server"""
        req = HaRequest(
            base_url=self.base_url,
            endpoint=endpoint,
            data=data
        )

        req.send()
    
    # def send_request_and_wait_response(self, req: HaRequest) -> HaResponse:
    #     """Send a service request and wait for a response"""
    #     # Construct service URL
    #     service_url = f"{self._url}{req.service_uri}"
        
    #     response = requests.post(service_url, headers=self._headers(), json=req.data)
        
    #     if response.status_code == 200: # Check response status
    #         return HaResponse(response.json())
    #     else:
    #         return HaResponse()
        