import time 
import RPi.GPIO as GPIO
import datetime
from Sun import Sun
#RPI.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

PIN_SWITCH_UP = 7
PIN_SWITCH_DOWN = 29
# Taster Rauf und Runter
GPIO.setup(7,GPIO.IN) # pin 7 -> Rauf 
GPIO.setup(29,GPIO.IN)# Pin 29 zum runterfahren 
# Relais Schaltungen
GPIO.setup(3 , GPIO.OUT) # pin 3 -> rauf
GPIO.setup(5 , GPIO.OUT) # pin 5 -> runter



#Use GPS Coordinats for morning open and evening close
coords = {'longitude' : 11.581981, 'latitude' : 48.135125 }
sun = Sun()

# print current time
print datetime.datetime.utcnow().time()
# Sunrise time UTC (decimal, 24 hour format)
time = sun.getSunriseTime( coords )['decimal']
hours = int(time)
minutes = (time*60) % 60
seconds = (time*3600) % 60

print("%d:%02d.%02d" % (hours, minutes, seconds))
# Sunset time UTC (decimal, 24 hour format)
time = sun.getSunsetTime( coords )['decimal']
hours = int(time)
minutes = (time*60) % 60
seconds = (time*3600) % 60
print("%d:%02d.%02d" % (hours, minutes, seconds))

IsAlreadyUp = False
IsAlreadyDown = False
#http://raspberrypiguide.de/howtos/raspberry-pi-gpio-how-to/# Dauerschleife
while 1:
    if (sun.getSunriseTime( coords )['decimal'] < )
    # 
    #prüfen ob Sonnenaufgang ist
    #prüfen ob Sonnenuntergang ist
    #prüfen ob RAUF gedrückt ist
    #prüfen ob RUNTER gedrückt ist 

    #warten
    time.sleep(0.1)