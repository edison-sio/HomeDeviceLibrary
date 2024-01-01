from hdl.hass.device import HassDevice
from hdl.hass.hass import HassComms


class HassMotionSensor(HassDevice):
    def __init__(self, entity_id: str, hass: HassComms) -> None:
        super().__init__(entity_id=entity_id, hass=hass)
    
    def is_detected(self) -> bool:
        """Check if motion detected"""
        return True
    