import requests
from typing import Any
from hdl.hass.const import (
    HassEndpoint,
    HassService,
    HassDomain, 
    DEFAULT_HOST, 
    DEFAULT_PORT
)
import json

class HassError(Exception):
    pass

class HassResponse:
    def __init__(self, host: str) -> None:
        self.host = host
        self.data: requests.Response | None = None
    
    def load(self, data: requests.Response) -> None:
        """Load the response data"""
        self.data = data
    
    @property
    def status_code(self) -> int:
        """Get the HTTP status code from the server"""
        if self.data is None:
            raise HassError("HassResponse: no response from Home Assistant loaded.")
        return self.data.status_code
    
    def ok(self) -> bool:
        """Check if response is HTTP 200 OK"""
        if self.status_code == 200:
            return True
        return False
    
    def json(self) -> dict:
        """Get the json format of the response data"""
        if self.data:
            return self.data.json()
        raise HassError("HassResponse: no response from Home Assistant loaded.")

class HassComms:
    def __init__(self, token: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:
        self._token = token
        self.host = host
        self.port = port
    
    def _check_api(self) -> None:
        """Check if Home Assistant API active"""
        

    def reset_token(self, token: str) -> None:
        """Reset token"""
        self._token = token
    
    def _headers(self, token: str) -> dict[str, str]:
        """Construct request headers"""
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    # def get_states(self) -> list[dict[str, Any]]:
    def get_states(self) -> Any:
        """Get a list of state objects"""
        res = self.get(
            endpoint=HassEndpoint.DEVICE_STATES
        )

        return res.json()
    
    def get_state(self, entity_id: str) -> dict[str, Any]:
        """Get state object of a device/entity"""
        res = self.get(
            endpoint=str(HassEndpoint.DEVICE_STATE).format(entity_id=entity_id)
        )

        return res.json()

    def get(self, endpoint: HassEndpoint | str, params: dict[str, str] | None = None, data: dict[str, str] | None = None) -> HassResponse:
        """Send get request to the HA server and get response"""
        url = f"http://{self.host}:{self.port}{endpoint}"
        res = requests.get(url, params=params, headers=self._headers(self._token), json=data)
        
        ha_res = HassResponse(self.host)
        ha_res.load(res)
        return ha_res
    
    def post(self, endpoint: HassEndpoint | str, params: dict[str, str] | None = None, data: dict[str, str] | None = None) -> HassResponse:
        """Send post request to the HA server and get response"""
        url = f"http://{self.host}:{self.port}{endpoint}"
        res = requests.post(url, params=params, headers=self._headers(self._token), json=data)

        ha_res = HassResponse(self.host)
        ha_res.load(res)
        return ha_res
    
    def call_service(self, domain: HassDomain, service: HassService, data: dict[str, str] | None = None) -> HassResponse:
        """Call a Home Assistant Service"""
        
        endpoint = f"{HassEndpoint.SERVICE}".format(domain=domain, service=service)

        res = self.post(endpoint=endpoint, data=data)
        return res

    def get_entity_ids(self, domain: HassDomain | str = "") -> list[str]:
        """Get call entity ids"""
        ids = []
        states = self.get_states()

        for state in states:
            try:

                entity_id = state["entity_id"]
                if entity_id.startswith(f"{domain}"):
                    ids.append(entity_id)
            except:
                continue
        
        return ids