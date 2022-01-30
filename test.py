import requests
import geopy.distance
import time
import sys
from time import sleep
from gpiozero import Buzzer
from datetime import datetime

#This code is released under the terms of the unlicense: https://unlicense.org/
#Author github.com/lexfp

running=True






BUZZER_PIN = 17
# seconds between each check                                                                                                               
buzzer = Buzzer(BUZZER_PIN)








def buzz(wait=0.1):
    print "Turning buzzer on"
    buzzer.on()
    print "sleeping"
    sleep(0.2)
    print "Turning buzzer off"
    buzzer.off()
    print "sleeping"
    sleep(0.2)
    print "returning"


try:
    print "Application started"
    while running:
        #checkRadar()
        print "calling buzz"
        sys.stdout.flush()
        buzz(0.1)
        time.sleep(1)

except (ValueError):
	#sometimes we get errors parsing json
    pass

except (KeyboardInterrupt):
    running = False
    print "Applications closed!"

except:
    print "Caught generic exception - continuing"
    sys.stdout.flush()
    pass

