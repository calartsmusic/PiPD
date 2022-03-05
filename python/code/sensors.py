#!/usr/bin/python3.9
import re
import time
import board
import busio
import random
import aqi
import os.path
from datetime import datetime
from time import sleep
#Sensor Libraries
import adafruit_mpl3115a2
import adafruit_tsl2561
import adafruit_htu21d
from gpiozero import MCP3008
from adafruit_pm25.i2c import PM25_I2C

counter = 0

#Define Sensors
i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) #Air Pressure - Altitude - Temperature
sensor2 = adafruit_tsl2561.TSL2561(i2c) #Ambient Light
sensor3 = adafruit_htu21d.HTU21D(i2c) #Humidity
pm25 = PM25_I2C(i2c) # Air Quality Index
spl = MCP3008(0)
soil = MCP3008(1)   #Capacitive Soil Sensor v1.2
sensor.sealevel_pressure = 102250
myaqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, '12', algo=aqi.ALGO_EPA)

def grab():
    #Create index number for each reading
    global counter
    global new_name
    counter += 1
    #Read each sensor
    spl = MCP3008(0)
    soil = MCP3008(1)
    pressure = sensor.pressure
    altitude = sensor.altitude
    temperature = sensor.temperature
    fahrenheit = (temperature * 9/5) + 32
    #lux = sensor2.lux
    lux = float(0 if sensor2.lux is None else sensor2.lux)
    broadband = sensor2.broadband
    infrared = sensor2.infrared
    luminosity = sensor2.luminosity
    humidity = sensor3.relative_humidity
    aqdata = pm25.read()
    myaqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, aqdata["pm25 standard"], algo=aqi.ALGO_EPA)
    #Strip the parenthesis and comma from the luminosity readings
    lumi = str(luminosity)
    lumi = re.sub("[()]", "", lumi)
    lumi =  re.sub("[,]", "", lumi)
    #Write the sensor data to a text file
    name = 'log-'+datetime.today().strftime('%m%d-%H:%M')+'.txt'
    if counter == 1:
        #name = 'log-'+datetime.today().strftime('%m%d-%H:%M')
        file = open(name,'a')
        new_name = str(name)
    else:
        file = open(new_name,'a')

    file.write(str(counter)+', ')
    file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S '))
    file.write('SPL {0:.2f}'.format(spl.value)+' ')
    file.write('Moisture {0:.4f}'.format(soil.value)+' ')
    file.write('Pressure {0:.4f}'.format(pressure)+' ')
    file.write('Altitude {0:.4f}'.format(altitude)+' ')
    file.write('Temperature {0:.4f}'.format(temperature)+' ')
    file.write('Fahrenheit {0:.4f}'.format(fahrenheit)+' ')
    file.write('Lux {0:.4f}'.format(lux)+' ')
    #file.write('Lux {butt}'.format(butt= sensor2.lux)+' ')
    file.write('Broadband {0:.2f}'.format(broadband)+' ')
    file.write('Infrared {0:.2f}'.format(infrared)+' ')
    file.write('Luminosity {}'.format(lumi)+' ')
    file.write('Humidity {0:.4f}'.format(humidity)+' ')
    file.write('AQI {0:.1f};'.format(myaqi)+'\n')
    file.close()

while True:
    #Read and write sensor data every two minutes
    grab()
    sleep(120)
