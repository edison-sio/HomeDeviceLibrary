import abc

class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._rgb = (r, g, b)
        self._check()
    
    @property
    def rgb(self) -> tuple[int, int, int]:
        """Get RGB property"""
        return self._rgb
    
    def _check(self):
        """Check if the RGB value valid"""
        for c in self._rgb:
            if c <= 0 or c >= 256:
                raise Exception(f"Color: Invalid RGB color: {self.rgb}")
            
    @property
    def rgb(self) -> tuple[int, int, int]:
        return self._rgb

class BaseLight(abc.ABC):
    """Abstract class to represent light control interface"""
    @abc.abstractmethod
    def turn_on(self) -> bool:
        """Set the light state to ON"""
        pass

    @abc.abstractmethod
    def turn_off(self) -> bool:
        """Set the light state to OFF"""
        pass
    
    @abc.abstractmethod
    def set_color(self, color: Color | tuple[int, int, int]) -> bool:
        """Set the light color"""
        pass
    
    @abc.abstractmethod
    def set_brightness(self, brightness: float) -> bool:
        """Set the light brightness"""
        pass