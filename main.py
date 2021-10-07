import circle as c
#importeert heel de file
import zwembad as z
#importeert enkel de Device klasse uit de file
from device import Device, DeviceManager

#roept achterliggend de __init__functie op
cirkel1 = c.Circle(2)
cirkel2 = c.Circle(5)


print(cirkel1)
print(cirkel1.omtrek())
print(cirkel2.omtrek())

pool = z.Zwembad(straal_zwembad=3,breedte_pad=0.5)
print(pool.prijs_omheining())
print(pool.prijs_pad())
print(pool.totaal())

device1 = Device("Lamp 1", False)
device2 = Device("Lamp 2", False)
device3 = Device("Philips hue", True)

device_manager = DeviceManager()
device_manager.add_device(4583, device1)
device_manager.add_device(78945, device2)

for id, device in device_manager.device_dict.items():
    print(id)
    print(device)