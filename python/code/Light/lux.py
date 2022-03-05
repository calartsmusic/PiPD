import board
import busio
import adafruit_tsl2561

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)

lux = float(0 if sensor.lux is None else sensor.lux)

print(lux)

print('Lux:{0:.4f}'.format(lux))
print('Broadband: {}'.format(sensor.broadband))
print('Infrared: {}'.format(sensor.infrared))
print('Luminosity: {}'.format(sensor.luminosity))
