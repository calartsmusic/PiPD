import time
import board
import adafruit_mpl3115a2
import adafruit_tsl2561
import adafruit_htu21d
import busio
import random
from pythonosc import udp_client
from gpiozero import MCP3008

#from adafruit_htu21d import HTU21D

#Setup the OSC Connection
ip = "127.0.0.1"
port = 5000
client = udp_client.SimpleUDPClient(ip, port)

# Initialize the i2c bus
i2c = board.I2C()

# Initialize the sensor boards
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor2 = adafruit_tsl2561.TSL2561(i2c)
sensor3 = adafruit_htu21d.HTU21D(i2c) 

# Define analog inputs to the MCP3008 ADC
pot1 = MCP3008(0)

# You can configure the pressure at sealevel to get better altitude estimates.
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 102250

# Main loop to read the sensor values and print them every second.
while True:
    #pressure = sensor.pressure
    #print("Pressure: {0:0.3f} pascals".format(pressure))
    client.send_message("/pressure", sensor.pressure)

    #altitude = sensor.altitude
    #print("Altitude: {0:0.3f} meters".format(altitude))
    client.send_message("/altitude", sensor.altitude)

    #temperature = sensor.temperature
    fahrenheit = (sensor.temperature * 9/5) + 32
    client.send_message("/temperature", fahrenheit)
    #print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    #print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit))

    #lux = sensor2.lux
    #print('Lux: {}'.format(lux))
    client.send_message("/lux", sensor2.lux)

    #broadband = sensor2.broadband
    #print('Broadband: {}'.format(broadband))
    client.send_message("/broadband", sensor2.broadband)

    #infrared = sensor2.infrared
    #print('Infrared: {}'.format(infrared))
    client.send_message("/infrared", sensor2.infrared)

    #luminosity = sensor2.luminosity
    #print('Luminosity: {}'.format(luminosity))
    client.send_message("/luminosity", sensor2.luminosity)

    temperature2 = sensor3.temperature
    fahrenheit2 = (temperature2 * 9/5) + 32
    #print('Temperature2:{0:0.3f} degrees Celsius'.format(temperature2))
    #print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit2))
    client.send_message("/temperature2", fahrenheit2)

    #humidity = sensor3.relative_humidity
    #print('Humidity: {}'.format(humidity))
    client.send_message("/humidity", sensor3.relative_humidity)

    #print(pot1.value)
    client.send_message("/pot1", pot1.value)

    #time.sleep(0.1)
    #print("########################")
