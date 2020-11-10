import RPi.GPIO as GPIO
import json
import os.path
import datetime
import time
import random

#set the GPIO to read the pins using the Broadcom SOC channel 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs (12 - 2, 2 are for environment manager)
pw = [21, 20, 16, 12, 7, 8, 25, 24, 23, 18] #GPIO21, etc

#define power plug pins as output and turn all channels OFF
#power plug relay is ON with low signal, and OFF with High sinal
for powerPlug in pw:
    GPIO.setup(powerPlug, GPIO.OUT)
#     GPIO.output(pw, GPIO.HIGH)

#get the time value and format
now = datetime.datetime.now()
timeString = now.strftime("%H")



def tideSimulation(settings):
    lastTide = int(settings["tideSettings"]["lastTide"])
    tideInterval = settings["tideSettings"]["tideInterval"]
    
    if lastTide + tideInterval <= int(timeString):
        settings["tideSettings"]["lastTide"] = timeString
        with open('powerPlugConfig.json', 'w') as file:
            json.dump(settings, file, indent=2)
        skimmerPlug = settings["skimmerSettings"]["skimmerPowerPlug"]
        GPIO.output(pw[skimmerPlug], GPIO.HIGH) #disable skimmer to prevent overflow
        pumpPlugs = settings["tideSettings"]["pumpPowerPlugs"]
        pumpPlugsTemp = pumpPlugs.copy(); #create a copy to remove the disabled pumps
        tideDuration = settings["tideSettings"]["tideDuration"]
        for x in range(0, len(pumpPlugsTemp)):
            disablePump = random.randint(0, len(pumpPlugsTemp)-1)
            GPIO.output(pw[pumpPlugsTemp.pop(disablePump)], GPIO.HIGH)
            time.sleep(tideDuration/3)
        time.sleep(tideDuration)
        for x in range(0, len(pumpPlugs)):
            GPIO.output(pw[pumpPlugs[x]], GPIO.HIGH)
        GPIO.output(pw[skimmerPlug], GPIO.LOW)
    


with open('powerPlugConfig.json', 'r') as json_file:
    data = json.load(json_file)
    for conf in data['settings']:
        if timeString == conf['time']: 
            for x in range(0, len(pw)):
                actuator="pw%d" % (x)
                if data["skimmerSettings"]["skimmerPowerPlug"] == x and data["skimmerSettings"]["delaySkimmerStart"] == True: #Configuration Enabled
                    if GPIO.input(pw[x]) == True and conf[actuator] == False: #Skimmer Power Plug Disabled set to enable
                        time.sleep(data["skimmerSettings"]["skimmerDelay"])                    #Wait 1m to enable  and GPIO.input(pw[x]) == 1
                GPIO.output(pw[x], conf[actuator])
               
if data['tideSettings']['tideSimulation'] == True:
    tideSimulation(data)