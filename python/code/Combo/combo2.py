import time
import board
import adafruit_mpl3115a2
import busio
import adafruit_tsl2561
import random
from pythonosc import udp_client

#Setup the OSC Connection

ip = "192.168.0.103"
port = 5000

client = udp_client.SimpleUDPClient(ip, port)

i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the MPL3115A2.
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor2 = adafruit_tsl2561.TSL2561(i2c)
# You can configure the pressure at sealevel to get better altitude estimates.
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 102250

# Main loop to read the sensor values and print them every second.
while True:
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} pascals".format(pressure))
    client.send_message("/pressure", pressure)

    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    client.send_message("/altitude", altitude)

    temperature = sensor.temperature
    fahrenheit = (temperature * 9/5) + 32
    client.send_message("/temperature", fahrenheit)
    print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit))

    lux = sensor2.lux
    print('Lux: {}'.format(sensor2.lux))
    client.send_message("/lux", lux)

    broadband = sensor2.broadband
    print('Broadband: {}'.format(sensor2.broadband))
    client.send_message("/broadband", broadband)

    infrared = sensor2.infrared
    print('Infrared: {}'.format(sensor2.infrared))
    client.send_message("/infrared", infrared)

    luminosity = sensor2.luminosity
    print('Luminosity: {}'.format(sensor2.luminosity))
    client.send_message("/luminosity", luminosity)

    time.sleep(.5)
    print("########################")
