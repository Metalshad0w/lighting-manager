import RPi.GPIO as GPIO
import json
import datetime
import random
import time

#set the GPIO to read the pins using the Broadcom SOC channel 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set the duty cicle for PWM
dutyCicle = 50

#define actuators GPIOs
ch = [26, 19, 13, 6] #GPIO26, GPIO19, GPIO13 and GPIO06
cooler = 5 #GPIO5

#define channel pins as output
GPIO.setup(ch[0], GPIO.OUT)
GPIO.setup(ch[1], GPIO.OUT)
GPIO.setup(ch[2], GPIO.OUT)
GPIO.setup(ch[3], GPIO.OUT)
GPIO.setup(cooler, GPIO.OUT)

#turn all channels OFF 
# GPIO.output(ch[0], GPIO.LOW)
# GPIO.output(ch[1], GPIO.LOW)
# GPIO.output(ch[2], GPIO.LOW)
# GPIO.output(ch[3], GPIO.LOW)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")


def cloudSimulation(desiredConfig, channelsNumber, cloudMaxTime):
    
    cloudTime = random.randint(0, cloudMaxTime)
    print(cloudTime)
    newConfig = desiredConfig.copy()
    signCH = []
    for x in range(0, channelsNumber):
        actuator="ch%d" % (x)
        if desiredConfig[actuator] > 0:
            newConfig[actuator] = random.randint(int(desiredConfig[actuator]/2), desiredConfig[actuator])
        else:
            newConfig[actuator] = desiredConfig[actuator]
        
        signCH.append(GPIO.PWM(ch[x],dutyCicle))
        signCH[x].start(newConfig[actuator])
    print(desiredConfig)
    print(newConfig)
    time.sleep(cloudTime)




with open('lightConfig.json') as json_file:
    data = json.load(json_file)
    for conf in data['settings']:
        if timeString == conf['time']:
            if data['cloudSettings']['cloudSimulation'] == True:
                cloudSimulation(conf, len(ch), data['cloudSettings']['cloudMaxTime'])
            signCH = []
            for x in range(0, len(ch)):
                actuator="ch%d" % (x)
                signCH.append(GPIO.PWM(ch[x],dutyCicle))
                signCH[x].start(conf[actuator])
                
if ch[0] == GPIO.LOW and ch[1] == GPIO.LOW and ch[2] == GPIO.LOW and ch[3] == GPIO.LOW:
    GPIO.output(cooler, GPIO.LOW)
else:
    GPIO.output(cooler, GPIO.HIGH)
    