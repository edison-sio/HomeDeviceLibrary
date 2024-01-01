from hdl.hass.hass import HassComms
from hdl.hass.light import HassLight
from hdl.hass.climate import HassClimate
from hdl.hass.factory import HassFactory
import requests
import json
import time

if __name__ == "__main__":
    # endpoint = "api/states/light.corridor_light"
    # url = f"http://192.168.1.18:8123/{endpoint}"
    token = "<your-token>"

    ip = "<your-ip-address>"

    ha = HassComms(token=token, host=ip)
    
    factory = HassFactory(token)
    devices = factory.get_devices()

    print(devices)

    # ac: HassClimate = devices["climate.living_room_a_c"]
    # gaming_light: HassLight = devices["light.gaming_light"]
    # corridor_light: HassLight = devices["light.corridor_light"]


    