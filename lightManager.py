import RPi.GPIO as GPIO
import json
import os.path
import datetime

#set the GPIO to read the pins using the Broadcom SOC channel 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set the duty cicle for PWM
dutyCicle = 50

#define actuators GPIOs
ch = [26, 19, 13, 6] #GPIO26, GPIO19, GPIO13 and GPIO06

#define channel pins as output
GPIO.setup(ch[0], GPIO.OUT)
GPIO.setup(ch[1], GPIO.OUT)
GPIO.setup(ch[2], GPIO.OUT)
GPIO.setup(ch[3], GPIO.OUT)

#turn all channels OFF 
GPIO.output(ch[0], GPIO.LOW)
GPIO.output(ch[1], GPIO.LOW)
GPIO.output(ch[2], GPIO.LOW)
GPIO.output(ch[3], GPIO.LOW)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")



def cloudSimulation(timeNow){
    for x in range(0, len(ch)):
        actuator="ch%d" % (x)
        print("CH%d: " % (x) + conf[actuator])
        signCH=GPIO.PWM(ch[x],dutyCicle)
        signCH.start(int(conf[actuator]))
    }




with open('lightConfig.json') as json_file:
    data = json.load(json_file)
    for conf in data['settings']:
        if timeString == conf['time']:        
            for x in range(0, len(ch)):
                actuator="ch%d" % (x)
                print("CH%d: " % (x) + conf[actuator])
                signCH=GPIO.PWM(ch[x],dutyCicle)
                signCH.start(int(conf[actuator]))