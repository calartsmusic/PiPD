from gpiozero import MCP3008
import time

pc = MCP3008(2)

while True:
    print('PC {0:.4f}'.format(pc.value)+' ')
    time.sleep(.01)
