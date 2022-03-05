from gpiozero import Button
from signal import pause

import os

def send2pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000")

def but1_on():
    print("Button 1: Down")
    message = 'but1 1;'
    send2pd(message)

def but1_off():
    print("Button 1: Up")
    message = 'but1 0;'
    send2pd(message)

def but2_on():
    print("Button 2: Down")
    message = 'but2 1;'
    send2pd(message)

def but2_off():
    print("Button 2: Up")
    message = 'but2 0;'
    send2pd(message)

def but3_on():
    print("Button 3: Down")
    message = 'but3 1;'
    send2pd(message)

def but3_off():
    print("Button 3: Up")
    message = 'but3 0;'
    send2pd(message)

def but4_on():
    print("Button 4: Down")
    message = 'but4 1;'
    send2pd(message)

def but4_off():
    print("Button 4: Up")
    message = 'but4 0;'
    send2pd(message)

def but5_on():
    print("Button 5: Down")
    message = 'but5 1;'
    send2pd(message)

def but5_off():
    print("Button 5: Up")
    message = 'but5 0;'
    send2pd(message)

def but6_on():
    print("Button 6: Down")
    message = 'but6 1;'
    send2pd(message)

def but6_off():
    print("Button 6: Up")
    message = 'but6 0;'
    send2pd(message)

button1 = Button(17)
button2 = Button(27)
button3 = Button(22)
button4 = Button(23)
button5 = Button(24)
button6 = Button(25)

button1.when_pressed = but1_on
button1.when_released = but1_off

button2.when_pressed = but2_on
button2.when_released = but2_off

button3.when_pressed = but3_on
button3.when_released = but3_off

button4.when_pressed = but4_on
button4.when_released = but4_off

button5.when_pressed = but5_on
button5.when_released = but5_off

button6.when_pressed = but6_on
button6.when_released = but6_off

pause()
