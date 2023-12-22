import requests
from typing import Any
from .const import HassEndpoint, DEFAULT_HOST, DEFAULT_PORT

class HassResponse:
    def __init__(self, host: str) -> None:
        self.host = host
        self._data = None
    
    def load(self, data: requests.Response) -> None:
        """Load the response data"""
        self._data = data
    
    def status_code(self) -> int:
        """Get the HTTP status code from the server"""
        ...
    
    def ok(self) -> bool:
        """Check if response is HTTP 200 OK"""
        ...
    
    def json(self) -> dict:
        """Get the json format of the response data"""
        ...

class HassComms:
    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, token: str | None = None) -> None:
        self.host = host
        self.port = port
        self._token = token # cache token
    
    def reset_token(self, token: str) -> None:
        """Reset token"""
        self._token = token
    
    def _headers(self, token: str) -> dict[str, str]:
        """Construct request headers"""
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    def get(self, endpoint: HassEndpoint | str, params: dict[str, str] | None, data: dict[str, str] | None = None) -> HassResponse:
        """Send get request to the HA server and get response"""
        url = f"http://{self.host}:{self.port}{endpoint}"
        res = requests.get(url, params=params, headers=self._headers(self._token), data=data)
        
        ha_res = HassResponse(self.host)
        ha_res.load(res)
        return ha_res
    
    def post(self, endpoint: HassEndpoint | str, params: dict[str, str] | None = None, data: dict[str, str] | None = None) -> HassResponse:
        """Send post request to the HA server and get response"""
        url = f"http://{self.host}:{self.port}{endpoint}"
        res = requests.post(url, params=params, headers=self._headers(self._token), data=data)
        
        ha_res = HassResponse(self.host)
        ha_res.load(res)
        return ha_res
    
    def _params_to_str(self, params: dict[str, str]) -> str:
        """Convert params to string as URL suffix"""
        if not params:
            return ""
        s = "?"
        for k, v in params:
            if s != "?":
                s += "&"
            s += f"{k}={v}"
        return s