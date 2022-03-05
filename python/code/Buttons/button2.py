import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

#initialise a previous input variable to 0 (assume button not pressed last)
but1_input = 0
while True:
  #take a reading
  but1 = GPIO.input(17)

  #if the last reading was low and this one high, print
  if ((not but1_input) and but1):
    print("Button pressed")
  #update previous input
  but1_input = but1
  #slight pause to debounce
  time.sleep(0.05)




#while True:
#    input_value = GPIO.input(17)
#    print(input_value)
#
#    if input_value == 0:
#        print('Who pressed my button!')
#        while input_value == False:
#            input_value = GPIO.input(17) 
