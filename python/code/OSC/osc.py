import argparse
import random
import time

from pythonosc import udp_client

ip = "192.168.0.103"
port = 5000

client = udp_client.SimpleUDPClient(ip, port)

for x in range(10):
  client.send_message("/filter", random.random())
  print('Value ' + str(x))
  time.sleep(1)
