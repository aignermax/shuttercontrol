import time 
#include <wiringPi.h>
import RPi.GPIO as GPIO
import datetime
from promise import Promise
from Sun import Sun

#RPI.GPIO Layout verwenden (wie Pin-Nummern)


PIN_SWITCH_UP = 7
PIN_SWITCH_DOWN = 29
PIN_RELAIS_UP = 3
PIN_RELAIS_DOWN = 5
# Taster Rauf und Runter
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_SWITCH_UP,GPIO.IN)# pin 7 -> Rauf 
GPIO.setup(PIN_SWITCH_DOWN,GPIO.IN)# Pin 29 zum runterfahren 
# Relais Schaltungen
GPIO.setup(PIN_RELAIS_UP, GPIO.OUT) # pin 3 -> rauf
GPIO.setup(PIN_RELAIS_DOWN, GPIO.OUT) # pin 5 -> runter
run()

def run():
    """the always running Loop - controls sunset sunrise and buttons"""
    #Use GPS Coordinats for morning open and evening close
    COORDS = {'longitude' : 11.581981, 'latitude' : 48.135125}
    SUN = Sun()
    lastUpDay = 0 # fur die sonnenstandAbfrage
    lastDownDay = 0
    hochfahren = 0
    runterfahren = 0
    buttonPressedUp = False
    buttonPressedDown = False
    buttonsLocked = False
    alterStatusHochfahren = False
    alterStatusRunterfahren = False
    StartzeitBewegung = 0
    #property GanzHochFahren -> setter -> if oldval == false && newval == true -> HochfahrenZeit = DateTime.Now
    #http://raspberrypiguide.de/howtos/raspberry-pi-gpio-how-to/# Dauerschleife 

    while 1:
        time.sleep(0.1)

        # Sonnenstand Abfragen 
        now = datetime.datetime.utcnow().time()
        sunrise = SUN.getSunriseTime(COORDS)['decimal']
        sunset = SUN.getSunsetTime(COORDS)['decimal']
        if sunrise < 6.5 - 1:
            sunrise = 6.5 - 1 # niemand will vor 6:30 aufgeweckt werden in dem fall, denk ich mal.. das -1 ist die Zeitzohne.
        if sunset > 22 - 1:
            sunset = 22 - 1

        if now > sunrise:
            if now < sunrise + 1/60:
                if datetime.datetime.now().day != lastUpDay:
                    lastUpDay = datetime.datetime.now().day
                    hochfahren = True
        if now > sunset:
            if now < sunset + 1/60:
                if datetime.datetime.now().day != lastDownDay:
                    lastDownDay = datetime.datetime.now().day
                    runterfahren = True

        # Taster Abfragen 
        if GPIO.input(PIN_SWITCH_UP):
            if not buttonsLocked:
                if not buttonPressedUp:
                    buttonPressedUp = True
                    StartzeitSwitchUp = datetime.datetime.now().time()
                else:
                    hochfahren = True
        else:
            buttonPressedUp = False
            if buttonPressedUp and now - StartzeitSwitchUp > 1/60/60 * 20:
                stop = True # stoppt sofort beim Loslassen, wenn Knopf nur kurz gedrueckt wurde.

        if GPIO.input(PIN_SWITCH_DOWN):
            if not buttonsLocked:
                if not buttonPressedDown:
                    buttonPressedDown = True
                    StartzeitSwitchDown = datetime.datetime.now().time()
                else:
                    hochfahren = True
        else:
            buttonPressedDown = False
            if buttonPressedDown and now - StartzeitSwitchDown > 1/60/60 * 20:
                stop = True # stoppt sofort beim Loslassen, wenn Knopf nur kurz gedrueckt wurde.

        if not buttonPressedUp and not buttonPressedDown:
            buttonsLocked = False

        # Relais setzen
        if hochfahren:
            if not alterStatusHochfahren:
                alterStatusHochfahren = True
                StartzeitBewegung = datetime.datetime.utcnow().time()
            runterfahren = False
            GPIO.output(PIN_RELAIS_DOWN, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(PIN_RELAIS_UP, GPIO.HIGH)
        elif runterfahren:
            if not alterStatusRunterfahren:
                alterStatusRunterfahren = True
                StartzeitBewegung = datetime.datetime.utcnow().time()
            hochfahren = False
            GPIO.output(PIN_RELAIS_UP, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(PIN_RELAIS_DOWN, GPIO.HIGH)

        if not hochfahren:
            alterStatusHochfahren = False
        if not runterfahren:
            alterStatusRunterfahren = False

        if stop:
            stop = False
            GPIO.output(PIN_RELAIS_DOWN, GPIO.LOW)
            GPIO.output(PIN_RELAIS_UP, GPIO.LOW)
            hochfahren = False
            runterfahren = False
            buttonsLocked = True

        if now - StartzeitBewegung > 1/60 /60 *20: # nach 20 Sekunden schaltet sich rauf/runter selber ab.
            stop = True
