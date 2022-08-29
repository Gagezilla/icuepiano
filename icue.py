from cuesdk import CueSdk
import asyncio, time

sdk = CueSdk()
sdk.connect()

class Devices:
    def __init__(self):
        self.devices = self.get_all_devices()

    def get_all_devices(self):
        devices = []
        for i in range(len(sdk.get_devices())):
            devices.append(Device(i))
        return devices

    def set_all_leds(self, rgb):
        for device in self.devices:
            device.set_leds(rgb)

    def flash_all_leds(self, rgb):
        for device in self.devices:
            device.flash_leds(rgb)

class Device:
    def __init__(self, index):
        self.device_index = index
        self.led_positions = sdk.get_led_positions_by_device_index(self.device_index)

    def set_leds(self, rgb):
        new_colors = {}
        for keyid in self.led_positions:
            new_colors[keyid] = rgb
        sdk.set_led_colors_buffer_by_device_index(self.device_index, new_colors)
        sdk.set_led_colors_flush_buffer()

    def flash_leds(self, rgb):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.flash_leds_f(rgb))

    async def flash_leds_f(self, rgb):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        while r != 0 and g != 0 and b != 0:
            if r > 0:
                r = r-1
            if g > 0:
                g = g-1
            if b > 0:
                b = b-1
            self.set_leds((r, g, b))


def get_all_devices():
    return sdk.get_devices()

def print_all_devices():
    print(sdk.get_devices())

def get_device_index(device_name):
    devices = sdk.get_devices()
    for i, device in enumerate(devices):
        if (device.__str__() == device_name):
            return i
