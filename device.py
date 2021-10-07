class Device:

    name:str = "default"
    is_on:bool = False

    def __init__(self, name, is_on):
        self.name= name
        self.is_on = is_on

    def switch_off(self):
        self.is_on = False

    def switch_on(self):
        self.is_on = True

    def toggle(self):
        self.is_on = not self.is_on

    def __str__(self) -> str:
        return self.name + " " + str(self.is_on)


class DeviceManager:

    def __init__(self):
        self.device_dict = {}

    def add_device(self, id, device):
        self.device_dict[id] = device

    def remove_device(self, id):
        self.device_dict.pop(id)

    def switch_everything_on(self):
        for id in self.device_dict:
            device = self.device_dict[id]
            device.switch_on()

    def switch_everything_off(self):
        for id in self.device_dict:
            device = self.device_dict[id]
            device.switch_off()

    def toggle_devices(self):
        for id in self.device_dict:
            device = self.device_dict[id]
            if device.is_on:
                device.switch_off()
            else:
                device.switch_on()