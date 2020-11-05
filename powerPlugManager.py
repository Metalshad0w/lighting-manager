import RPi.GPIO as GPIO
import json
import os.path
import datetime

#set the GPIO to read the pins using the Broadcom SOC channel 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
pw1 = 21 #GPIO21
pw2 = 20 #GPIO20
pw3 = 16 #GPIO16
pw4 = 12 #GPIO12
pw5 = 7  #GPIO07
pw6 = 8  #GPIO08
pw7 = 25 #GPIO25
pw8 = 24 #GPIO24
pw9 = 23 #GPIO23
pw10 = 18 #GPIO18
pw11 = 15 #GPIO15
pw12 = 14 #GPIO14


#define power plug pins as output
GPIO.setup(pw1, GPIO.OUT)
GPIO.setup(pw2, GPIO.OUT)
GPIO.setup(pw3, GPIO.OUT)
GPIO.setup(pw4, GPIO.OUT)
GPIO.setup(pw5, GPIO.OUT)
GPIO.setup(pw6, GPIO.OUT)
GPIO.setup(pw7, GPIO.OUT)
GPIO.setup(pw8, GPIO.OUT)
GPIO.setup(pw9, GPIO.OUT)
GPIO.setup(pw10, GPIO.OUT)
GPIO.setup(pw11, GPIO.OUT)
GPIO.setup(pw12, GPIO.OUT)

#turn all channels OFF 
GPIO.output(pw1, GPIO.LOW)
GPIO.output(pw2, GPIO.LOW)
GPIO.output(pw3, GPIO.LOW)
GPIO.output(pw4, GPIO.LOW)
GPIO.output(pw5, GPIO.LOW)
GPIO.output(pw6, GPIO.LOW)
GPIO.output(pw7, GPIO.LOW)
GPIO.output(pw8, GPIO.LOW)
GPIO.output(pw9, GPIO.LOW)
GPIO.output(pw10, GPIO.LOW)
GPIO.output(pw11, GPIO.LOW)
GPIO.output(pw12, GPIO.LOW)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")

with open('powerPlugConfig.json') as json_file:
    data = json.load(json_file)
    for conf in data['settings']:
        if timeString == conf['time']: 
            print('Time: ' + conf['time'])
            print('PW1: ' + conf['pw1'])
            print('PW2: ' + conf['pw2'])
            print('PW3: ' + conf['pw3'])
            print('PW4: ' + conf['pw4'])
            print('PW5: ' + conf['pw5'])
            print('PW6: ' + conf['pw6'])
            print('PW7: ' + conf['pw7'])
            print('PW8: ' + conf['pw8'])
            print('PW9: ' + conf['pw9'])
            print('PW10: ' + conf['pw10'])
            print('PW11: ' + conf['pw11'])
            print('PW12: ' + conf['pw12'])
            print('')
            
            GPIO.output(actuator, GPIO.HIGH)
