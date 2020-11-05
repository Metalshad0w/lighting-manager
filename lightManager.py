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
ch1 = 26 #GPIO26
ch2 = 19 #GPIO19
ch3 = 13 #GPIO13
ch4 = 6  #GPIO06

#define channel pins as output
GPIO.setup(ch1, GPIO.OUT)
GPIO.setup(ch2, GPIO.OUT)
GPIO.setup(ch3, GPIO.OUT)
GPIO.setup(ch4, GPIO.OUT)

#turn all channels OFF 
GPIO.output(ch1, GPIO.LOW)
GPIO.output(ch2, GPIO.LOW)
GPIO.output(ch3, GPIO.LOW)
GPIO.output(ch4, GPIO.LOW)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")


with open('lightConfig.json') as json_file:
    data = json.load(json_file)
    for conf in data['settings']:
        if timeString == conf['time']: 
            print('Time: ' + conf['time'])
            print('CH1: ' + conf['ch1'])
            print('CH2: ' + conf['ch2'])
            print('CH3: ' + conf['ch3'])
            print('CH4: ' + conf['ch4'])
            print('')
            
            signCH1=GPIO.PWM(ch1,dutyCicle)
            signCH1.start(int(conf['ch1']))
            signCH1=GPIO.PWM(ch2,dutyCicle)
            signCH1.start(int(conf['ch2']))
            signCH1=GPIO.PWM(ch3,dutyCicle)
            signCH1.start(int(conf['ch3']))
            signCH1=GPIO.PWM(ch4,dutyCicle)
            signCH1.start(int(conf['ch4']))