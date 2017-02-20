import time 
import signal
import sys
#include <wiringPi.h>
import RPi.GPIO as GPIO
import datetime
from Sun import Sun


#RPI.GPIO Layout verwenden (wie Pin-Nummern)

def now ():
    """returns the current time in floated hours. 11.5000 means 11 hours, 30 Minutes """
    mynow = datetime.datetime.utcnow().time()
    output = 0.0 + mynow.hour +(0.0 +  mynow.minute)/60 + (0.0 + mynow.second)/3600
    # print "now-time: " + str(output)
    return output

GPIO_PRESSED = False # false means pressed..
RELAISOFF = True #yes it is that mixed up with my relais..
RELAISON = False
PIN_SWITCH_UP = 7
PIN_SWITCH_DOWN = 29
PIN_RELAIS_UP = 3
PIN_RELAIS_DOWN = 5

# catch STRG+C command
def sign_handler(signal,frame):
    print('you pressed CTRL+C!')
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, sign_handler)
# Taster Rauf und Runter
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_SWITCH_UP,GPIO.IN)# pin 7 -> Rauf 
GPIO.setup(PIN_SWITCH_DOWN,GPIO.IN)# Pin 29 zum runterfahren 
# Relais Schaltungen
GPIO.setup(PIN_RELAIS_UP, GPIO.OUT) # pin 3 -> rauf
GPIO.setup(PIN_RELAIS_DOWN, GPIO.OUT) # pin 5 -> runter
GPIO.output(PIN_RELAIS_UP, RELAISOFF) # Relaises auschalten
GPIO.output(PIN_RELAIS_DOWN , RELAISOFF)

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
alterStatusStop = False
StartzeitBewegung = 0.0
StartzeitSwitchUp = 0.0
StartzeitSwitchDown = 0.0
stop = False
mynow = 0.0
sunrise = 0.0
sunset = 0.0

#property GanzHochFahren -> setter -> if oldval == false && newval == true -> HochfahrenZeit = DateTime.Now
#http://raspberrypiguide.de/howtos/raspberry-pi-gpio-how-to/# Dauerschleife 

while 1:
    time.sleep(0.1)

    # Sonnenstand Abfragen 
    mynow =  now()
    sunrise = SUN.getSunriseTime(COORDS)['decimal']
    sunset = SUN.getSunsetTime(COORDS)['decimal']
    if sunrise < 6.5 - 1:
        sunrise = 6.5 - 1 # niemand will vor 6:30 aufgeweckt werden in dem fall, denk ich mal.. das -1 ist die Zeitzohne.
    if sunset > 22 - 1:
        sunset = 22 - 1
    #mynow = (sunrise +(0.033333))
    
    if mynow > sunrise:
        print "mynow > sunrise"
        if mynow < sunrise + 0.0666:
            print "mynow < sunrise + 0.0666 + " + str(datetime.datetime.today().day) + " " + str(lastUpDay)
            if datetime.datetime.today().day != lastUpDay:
                lastUpDay = datetime.datetime.today().day
                hochfahren = True
		print "Sunrise detected"
    if mynow > sunset:
        if mynow < sunset + 0.0666:
            if datetime.datetime.today().day != lastDownDay:
                lastDownDay = datetime.datetime.today().day
                runterfahren = True
		print "Sunset detected"

    # Taster Abfragen 
    if True:
        if GPIO.input(PIN_SWITCH_UP)== GPIO_PRESSED:
	    print "up switch pressed ->Lock: " + str(buttonsLocked)
            if not buttonsLocked:
                if not buttonPressedUp:
                    buttonPressedUp = True
                    StartzeitSwitchUp = now()
		    print "StartzeitSwitchUp set: " + str( StartzeitSwitchUp)
                else:
                    hochfahren = True
	            print "up switch -> Hochfahren Init"
        else:
	    print "up switch released. timedif: " + str( mynow - StartzeitSwitchUp)
            if buttonPressedUp and mynow - StartzeitSwitchUp < 1/60/60 * 20:
	        print "up switch Stop"
                stop = True # stoppt sofort beim Loslassen, wenn Knopf nur kurz gedrueckt wurde.
	    buttonPressedUp = False

        if GPIO.input(PIN_SWITCH_DOWN)==GPIO_PRESSED:
	    print "down switch pressed ->Lock: " + str(buttonsLocked)
            if not buttonsLocked:
                if not buttonPressedDown:
                    buttonPressedDown = True
                    StartzeitSwitchDown = now()
                else:
                    hochfahren = True
		    print "down switch --> Runterfahren Init"
        else:
	    print "down switch released -> timedif: " + str(mynow - StartzeitSwitchDown)
            if buttonPressedDown and mynow - StartzeitSwitchDown < 1/60/60 * 20:
	        print "down switch Stop"
                stop = True # stoppt sofort beim Loslassen, wenn Knopf nur kurz gedrueckt wurde.
	    buttonPressedDown = False

    if not buttonPressedUp and not buttonPressedDown:
        buttonsLocked = False

    # Relais setzen
    if hochfahren:
	print "Go Up"
        if not alterStatusHochfahren:
            alterStatusHochfahren = True
            StartzeitBewegung = now()
        runterfahren = False
        GPIO.output(PIN_RELAIS_DOWN, RELAISOFF)
        time.sleep(0.2)
        GPIO.output(PIN_RELAIS_UP, RELAISON)
    elif runterfahren:
	print "Go Down"
        if not alterStatusRunterfahren:
            alterStatusRunterfahren = True
            StartzeitBewegung = now()
        hochfahren = False
        GPIO.output(PIN_RELAIS_UP, RELAISOFF)
        time.sleep(0.2)
        GPIO.output(PIN_RELAIS_DOWN, RELAISON)

    if not hochfahren:
        alterStatusHochfahren = False
    if not runterfahren:
        alterStatusRunterfahren = False

    if stop:
	if alterStatusStop == False:
	    alterStatusStop = True
    	    print "stop"
        stop = False
        GPIO.output(PIN_RELAIS_DOWN, RELAISOFF)
        GPIO.output(PIN_RELAIS_UP, RELAISOFF)
        hochfahren = False
        runterfahren = False
        buttonsLocked = True
    else:
        alterStatusStop = False

    if mynow - StartzeitBewegung > 1/60 /60 *20: # nach 20 Sekunden schaltet sich rauf/runter selber ab.
        stop = True
