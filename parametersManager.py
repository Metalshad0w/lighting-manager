import RPi.GPIO as GPIO
import json
import os
import datetime

#set the GPIO to read the pins using the Broadcom SOC channel 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
ch = [15, 14] #GPIO15, GPIO14

#define channel pins as output
GPIO.setup(ch[0], GPIO.OUT)
GPIO.setup(ch[1], GPIO.OUT)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")

print(os.environ['HOME'])