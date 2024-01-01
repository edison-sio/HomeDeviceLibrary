import abc

class BaseClimate(abc.ABC):
    """Abstract class to represent climate control interface"""
    def set_temperature(self, temp: int) -> bool:
        """Set temperature"""
        pass