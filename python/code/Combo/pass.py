import time
import board
import adafruit_mpl3115a2
import adafruit_tsl2561
import adafruit_htu21d
import busio
import random
from gpiozero import MCP3008

i2c = board.I2C()

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor2 = adafruit_tsl2561.TSL2561(i2c)
sensor3 = adafruit_htu21d.HTU21D(i2c) 

soil = MCP3008(7)
sensor.sealevel_pressure = 102250

while True:
    print('Spoil Moisture: {}'.format(soil.value))
    print(' ' )
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} pascals".format(pressure))

    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))

    temperature = sensor.temperature
    fahrenheit = (temperature * 9/5) + 32
    print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit))
    print(' ' )

    lux = sensor2.lux
    print('Lux: {}'.format(lux))

    broadband = sensor2.broadband
    print('Broadband: {}'.format(broadband))

    infrared = sensor2.infrared
    print('Infrared: {}'.format(infrared))

    luminosity = sensor2.luminosity
    print('Luminosity: {}'.format(luminosity))
    print(' ' )

    temperature2 = sensor3.temperature
    fahrenheit2 = (temperature2 * 9/5) + 32
    print('Temperature2:{0:0.3f} degrees Celsius'.format(temperature2))
    print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit2))

    humidity = sensor3.relative_humidity
    print('Humidity: {}'.format(humidity))

    time.sleep(2)
    print('        ')
    print('########################')
    print('        ')
