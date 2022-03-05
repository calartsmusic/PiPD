import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

#initialise a previous input variable to 0 (assume button not pressed last)
but1_input = 0
but2_input = 0
but3_input = 0

while True:
  #take a reading
  but1 = GPIO.input(17)
  but2 = GPIO.input(27)
  but3 = GPIO.input(22)

# print(but1)
  #if the last reading was low and this one high, print
  if ((not but1_input) and but1):
    print("But 1 pressed")
  #update previous input
  but1_input = but1
  #slight pause to debounce
  time.sleep(0.05)

  if ((not but2_input) and but2):
    print("But 2 pressed")
  but2_input = but2
  time.sleep(0.05)

  if ((not but3_input) and but3):
    print("But 3 pressed")
  but3_input = but3
  time.sleep(0.05)



#while True:
#    input_value = GPIO.input(17)
#    print(input_value)
#
#    if input_value == 0:
#        print('Who pressed my button!')
#        while input_value == False:
#            input_value = GPIO.input(17) 
