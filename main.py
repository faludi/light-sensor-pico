from wifi_network import WiFi
from thingspeak import ThingSpeakApi
from time import sleep
import qwiic_veml6030
from machine import Pin

status_led = Pin("LED", Pin.OUT)
status_led.on()
sleep(0.5)
status_led.off()

#Sensor Initialization
light_sensor = qwiic_veml6030.QwiicVEML6030()
if light_sensor.is_connected() == False:
    print("The device isn't connected to the system. Please check your connection", \
        file=sys.stderr)

# Initialize the device
light_sensor.begin()

#ThingSpeak Initialization
thingspeak = ThingSpeakApi()

#Network Initialization
network = WiFi()
ip = network.connect()

#Main Program
while True:
    ambient_light = light_sensor.read_light()
    print("Lux:\t%.1f" % ambient_light)
    thingspeak.write_single_field(ambient_light)
    status_led.on()
    sleep(0.1)
    status_led.off()
    sleep(16)