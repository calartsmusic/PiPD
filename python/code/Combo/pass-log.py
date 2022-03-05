import time
from time import sleep
import board
import adafruit_mpl3115a2
import adafruit_tsl2561
import adafruit_htu21d
import busio
import random
from gpiozero import MCP3008
from datetime import datetime

i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor2 = adafruit_tsl2561.TSL2561(i2c)
sensor3 = adafruit_htu21d.HTU21D(i2c) 
soil = MCP3008(7)
sensor.sealevel_pressure = 102250

def grab():
    soil = MCP3008(7)
    pressure = sensor.pressure
    altitude = sensor.altitude
    temperature = sensor.temperature
    fahrenheit = (temperature * 9/5) + 32

    file = open("pass.txt","a")
    file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S  '))
    file.write('Moisture {0:.4f};'.format(soil.value)+"\n")
    file.write('Pressure {0:.4f};'.format(pressure)+"\n")
    file.write('Altitude {0:.4f};'.format(altitude)+"\n")
    file.write('Temperature {0:.4f};'.format(temperature)+"\n")
    file.write('Fahrenheit {0:.4f};'.format(fahrenheit)+"\n")
    file.close()

    #print('Soil {0:.4f}; '.format(soil.value))
    #print('################')


while True:
    grab()
    sleep(5)


    #print('Spoil Moisture: {}'.format(soil.value))
    #print(' ' )
    #pressure = sensor.pressure
    #print("Pressure: {0:0.3f} pascals".format(pressure))

    #altitude = sensor.altitude
    #print("Altitude: {0:0.3f} meters".format(altitude))

    #temperature = sensor.temperature
    #fahrenheit = (temperature * 9/5) + 32
    #print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    #print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit))
    #print(' ' )

    #lux = sensor2.lux
    #print('Lux: {}'.format(lux))

    #broadband = sensor2.broadband
    #print('Broadband: {}'.format(broadband))

   # infrared = sensor2.infrared
    #print('Infrared: {}'.format(infrared))

   # luminosity = sensor2.luminosity
   # print('Luminosity: {}'.format(luminosity))
   # print(' ' )

   # temperature2 = sensor3.temperature
   # fahrenheit2 = (temperature2 * 9/5) + 32
   # print('Temperature2:{0:0.3f} degrees Celsius'.format(temperature2))
  #  print("Temperature: {0:0.3f} degrees Fahrenheit".format(fahrenheit2))

 #   humidity = sensor3.relative_humidity
#    print('Humidity: {}'.format(humidity))

  #  time.sleep(2)
  #  print('        ')
  #  print('########################')
  #  print('        ')
