import time
import board
import busio
from adafruit_pm25.i2c import PM25_I2C
import aqi

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
pm25 = PM25_I2C(i2c)

myaqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, '12', algo=aqi.ALGO_EPA)

print("Found PM2.5 sensor, reading data...")

while True:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        myaqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, aqdata["pm25 standard"], algo=aqi.ALGO_EPA)

    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    if ((myaqi >= 0)and (myaqi <= 50)):
        print("AQI = %d - - GOOD" %(myaqi))
    elif ((myaqi >= 51) and (myaqi <= 100)):
        print("AQI = %d - - MODERATE" %(myaqi))
    elif ((myaqi >= 101) and (myaqi <= 150)):
        print("AQI = %d - - UNHEALTHY FOR SENSITIVE GROUPS" %(myaqi))
    elif ((myaqi >= 151) and (myaqi <= 200)):
        print("AQI = %d - - UNHEALTHY" %(myaqi))
    elif ((myaqi >= 201) and (myaqi <= 300)):
        print("AQI = %d - - VERY UNHEALTHY" %(myaqi))
    elif ((myaqi >= 301)):
        print("AQI = %d - - HAZARDOUS" %(myaqi))
