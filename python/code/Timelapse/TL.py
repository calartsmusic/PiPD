#!/usr/bin/env python

# Import some frameworks
import os
import time
#import RPi.GPIO as GPIO
from datetime import datetime

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
s1 = d.strftime("%m%d-%H:%M")

# Define the location where you wish to save files.

folderToSave = str(s1)
os.mkdir(folderToSave)

# Set the initial serial for saved images to 1
fileSerial = 1

# Run a WHILE Loop of infinitely
while True:

    d = datetime.now()
    if d.hour > 0:

        # Set FileSerialNumber to 000X using four digits
        fileSerialNumber = "%04d" % (fileSerial)

        # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)

        # Define the size of the image you wish to capture.
        imgWidth = 2592 # Max = 2592
        imgHeight = 1944 # Max = 1944
        print(" Saving file at " + hour + ":" + mins)

        # Capture the image using raspistill. Set to capture with added sharpening, auto white balance and average metering mode
        # Change these settings where you see fit and to suit the conditions you are using the camera in
        os.system("raspistill -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/" + str(fileSerialNumber) +  ".png -vf -hf -q 100 -e png -sh 50 -sa -100 -co 35 -awb auto -ex auto -mm average -v")

        # Increment the fileSerial
        fileSerial += 1

        # Wait 10 seconds before next capture
        time.sleep(2)

    else:
        # Just trapping out the WHILE Statement
        print ("Doing nothing at this time")
