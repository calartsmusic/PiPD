from RPLCD.i2c import CharLCD
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
lcd = CharLCD('PCF8574', 0x27)

GPIO.setup(17, GPIO.IN)

lcd.backlight_enabled = (True)

lcd.cursor_mode = 'blink'
lcd.write_string('P1')
lcd.cursor_pos = (0,4)
lcd.write_string('P2')
lcd.cursor_pos = (0,8)
lcd.write_string('P3')
lcd.cursor_pos = (0,0)
sleep(5)

counter = 0
def bcount():
      global counter
      counter += 1
      print(counter)


while True:
    input_value = GPIO.input(17)
    if input_value == False:
        bcount()
        if counter == 1:
           lcd.cursor_pos = (0,4)
        elif counter == 2:
           lcd.cursor_pos = (0,8)
        else:
           counter = 0
           lcd.cursor_pos = (0,0) 
        while input_value == False:
            input_value = GPIO.input(17) 




#sleep(5)
#lcd.cursor_pos = (0,4)
#sleep(5)
#lcd.cursor_pos = (0,8)
#sleep(5)
#lcd.clear()

