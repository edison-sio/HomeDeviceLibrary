import enum

DEFAULT_HOST = "homeassistant.local"
DEFAULT_PORT = 8123

class HassEndpoint(enum.Enum):
    """This class stores Home Assistant API endpoints"""
    def __str__(self) -> str:
        return self.value

    DEVICE_STATE  = "/api/states/{entity_id}"
    DEVICE_STATES = "/api/states"
    ...

class HassDeviceState(enum.Enum):
    """This class stores device state"""
    def __str__(self) -> str:
        return self.value

class HassLightState(HassDeviceState):
    """Light state"""
    ON  = "on"
    OFF = "off"