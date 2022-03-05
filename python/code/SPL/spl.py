from gpiozero import MCP3008
import time

spl = MCP3008(0)

while True:
    print('SPL {0:.4f}'.format(spl.value)+' ')
    time.sleep(.3)

