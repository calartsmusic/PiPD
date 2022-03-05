from gpiozero import MCP3008
import time

spl = MCP3008(0)
soil = MCP3008(1)   #Capacitive Soil Sensor v1.2

while True:
    #print('SPL {0:.4f}'.format(spl.value)+' ')
    print('Moisture {0:.4f}'.format(soil.value)+' ')
    time.sleep(.3)

