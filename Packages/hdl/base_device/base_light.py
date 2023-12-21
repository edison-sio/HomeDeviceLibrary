import abc

class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self._rgb = (r, g, b)
    
    def _check(self):
        """Check if the RGB value valid"""
        for c in self._rgb:
            if c <= 0 or c >= 256:
                raise Exception(f"Invalid RGB color: {self.rgb}")
            
    @property
    def rgb(self) -> tuple[int, int, int]:
        return self._rgb

class BaseLight(abc.ABC):
    """Abstract class to represent light control"""
    @abc.abstractmethod
    def set_on(self) -> bool: ...
    
    @abc.abstractmethod
    def set_off(self) -> bool: ...
    
    @abc.abstractmethod
    def set_color(self, color: Color | tuple[int, int, int]) -> bool: ...
    
    @abc.abstractmethod
    def set_brightness(self, brightness: float) -> bool: ...
    