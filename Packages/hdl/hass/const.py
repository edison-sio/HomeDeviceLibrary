import enum

DEFAULT_HOST = "homeassistant.local"
DEFAULT_PORT = 8123

class HassEndpoint(enum.Enum):
    """This class stores Home Assistant API endpoints"""
    def __str__(self) -> str:
        return self.value

    DEVICE_STATE  = "/api/states/{entity_id}"
    DEVICE_STATES = "/api/states"
    
    # service APIs
    SERVICE = "/api/services/{domain}/{service}"

class HassDomain(enum.Enum):
    """Home Assistant Domains"""
    def __str__(self) -> str:
        return self.value

    ALARM_CONTROL_PANEL = "alarm_control_panel"
    AUTOMATION = "automation"
    INPUT_BOOLEAN = "input_boolean"
    REMOTE = "remote"
    SCRIPT = "script"
    BINARY_SENSOR = "binary_sensor"
    CLIMATE = "climate"
    COVER = "cover"
    DEVICE_TRACKER = "device_tracker"
    FAN = "fan"
    LIGHT = "light"
    LOCK = "lock"
    MEDIA_PLAYER = "media_player"
    SENSOR = "sensor"
    SWITCH = "switch"

class HassService(enum.Enum):
    """Home Assistant Services"""
    def __str__(self) -> str:
        return self.value

    TURN_ON = "turn_on"
    TURN_OFF = "turn_off"
    TOGGLE = "toggle"
    PRESS = "press"
    SET_AUX_HEAT = "set_aux_heat"
    SET_PRESET_MODE = "set_present_mode"
    SET_TEMPERATURE = "set_temperature"
    SET_HUMIDITY = "set_humidity"
    SET_FAN_MODE = "set_fan_mode"
    SET_HVAC_MODE = "set_hvac_mode"
    SET_SWING_MODE = "set_swing_mode"
    # TODO: more services to be added below...

class HassDeviceState(enum.Enum):
    """This class stores device state"""
    def __str__(self) -> str:
        return self.value

