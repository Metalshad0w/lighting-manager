import RPi.GPIO as GPIO
import json
import os.path
import datetime

#set the GPIO to read the pins using the Broadcom SOC channel 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
pw = [21, 20, 16, 12, 7, 8, 25, 24, 23, 18, 15, 14] #GPIO21, etc

#define power plug pins as output and turn all channels OFF 
for powerPlug in pw:
    GPIO.setup(pw, GPIO.OUT)
    GPIO.output(pw, GPIO.LOW)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")

with open('powerPlugConfig.json') as json_file:
    data = json.load(json_file)
    for conf in data['settings']:
        if timeString == conf['time']: 
            for x in range(0, len(pw)):
                actuator="pw%d" % (x)
                print(conf['time'])
                status = GPIO.HIGH
                print(status)
                GPIO.output(pw[x], status)
