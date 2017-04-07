import logging
import time 
import signal
import sys
#include <wiringPi.h>
import RPi.GPIO as GPIO
import datetime
from Sun import Sun


# setup logging 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/home/pi/Documents/Projects/rolladensteuerung/shuttercontrol/LOGshuttercontrol.log',
                    filemode='w')
#RPI.GPIO Layout verwenden (wie Pin-Nummern)

def now ():
    """returns the current time in floated hours. 11.5000 means 11 hours, 30 Minutes """
    mynow = datetime.datetime.utcnow().time()
    output = 0.0 + mynow.hour +(0.0 +  mynow.minute)/60 + (0.0 + mynow.second)/3600
    # print "now-time: " + str(output)
    return output

def timeZoneOffset():
    """returns the difference of the timezone and UTC also considering summer time"""
    is_dst = time.daylight and time.localtime().tm_isdst > 0
    utc_offset = 0.0 - (time.altzone if is_dst else time.timezone)
    return utc_offset /60.0/60.0

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

#Use GPS Coordinats for morning open and evening close
COORDS = {'longitude' : 11.581981, 'latitude' : 48.135125}
SUN = Sun()
lastUpDay = datetime.datetime.today().day -1 # fur die sonnenstandAbfrage
lastDownDay = datetime.datetime.today().day -1
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
debugcounter = 0
minhochzeit = 6.7

#property GanzHochFahren -> setter -> if oldval == false && newval == true -> HochfahrenZeit = DateTime.Now
#http://raspberrypiguide.de/howtos/raspberry-pi-gpio-how-to/# Dauerschleife 
print "start shuttercontrol. Welcome :)"
logging.info("start shuttercontrol. Welcome :)")

while 1:
    time.sleep(0.1)

    # Sonnenstand Abfragen 
    mynow =  now()
    sunrise = SUN.getSunriseTime(COORDS)['decimal']
    sunset = SUN.getSunsetTime(COORDS)['decimal']
    if datetime.datetime.today().weekday() > 4:
        minhochzeit = (8.0 - timeZoneOffset())
    else:
        minhochzeit = (6.70 - (timeZoneOffset()*2.0))
    debugcounter = debugcounter +1

    # werte anzeigen
    if debugcounter % 200 == 0:
        logging.info( "sunrise " + str(sunrise) + " minhoch " + str(minhochzeit) + " timezoneoff " + str(timeZoneOffset()) + " mynow " +  str(mynow) + " 6.7 - timeZ " + str(6.7-timeZoneOffset()) + " dayOW: " + str(datetime.datetime.today().weekday()))

    if sunrise < minhochzeit:
        sunrise = minhochzeit # niemand will vor 7 aufgeweckt werden in dem fall, denk ich mal.. das -1 ist die Zeitzohne.
    if sunset > 22.0 - timeZoneOffset():
        sunset = (22.0 - timeZoneOffset())

    if mynow > sunrise:
        if mynow < sunrise + 0.0666:
            if datetime.datetime.today().day != lastUpDay:
                lastUpDay = datetime.datetime.today().day
                GPIO.output(PIN_RELAIS_DOWN, RELAISOFF)
                hochfahren = True
                logging.info( "Sunrise detected " + sunrise + " now: " + mynow)
    if mynow > sunset:
        if mynow < sunset + 0.0666:
            if datetime.datetime.today().day != lastDownDay:
                lastDownDay = datetime.datetime.today().day
                GPIO.output(PIN_RELAIS_UP, RELAISOFF)
                runterfahren = True
                logging.info("Sunset detected " + sunset + " now: " + sunset)

    # Taster Abfragen 
    if True:
        if GPIO.input(PIN_SWITCH_UP)== GPIO_PRESSED:
            logging.info("up switch pressed ->Lock: " + str(buttonsLocked))
            if not buttonsLocked:
                if not buttonPressedUp:
                    buttonPressedUp = True
                    StartzeitSwitchUp = now()
                    logging.info("StartzeitSwitchUp set: " + str( StartzeitSwitchUp))
                else:
                    hochfahren = True
                    logging.info("up switch -> Hochfahren Init")
        else:
            if buttonPressedUp and mynow - StartzeitSwitchUp < 1.0/60.0/60.0 * 2.0:
                logging.info( "up switch Stop -> timedif: " + str( mynow - StartzeitSwitchUp))
                stop = True # stoppt sofort beim Loslassen, wenn Knopf nur kurz gedrueckt wurde.
            buttonPressedUp = False

        if GPIO.input(PIN_SWITCH_DOWN)==GPIO_PRESSED:
	    logging.info( "down switch pressed ->Lock: " + str(buttonsLocked))
            if not buttonsLocked:
                if not buttonPressedDown:
                    buttonPressedDown = True
                    StartzeitSwitchDown = now()
                else:
                    runterfahren = True
		    logging.info("down switch --> Runterfahren Init")
        else:
            #wenn knopf zwei sekunden gedrueckt war wird nicht gestoppt. 
            # die MaxZeit stoppt in diesem Fall (ganz unten)
            if buttonPressedDown and mynow - StartzeitSwitchDown < 1.0/60.0/60.0 * 2.0:
                logging.info("down switch Stop -> timedif: " + str(mynow - StartzeitSwitchDown))
                stop = True # stoppt sofort beim Loslassen, wenn Knopf nur kurz gedrueckt wurde.
            buttonPressedDown = False

    if (not buttonPressedUp and not buttonPressedDown) and buttonsLocked == True:
        buttonsLocked = False
        logging.info("set buttonLocked = " + str(buttonsLocked))

    # Relais setzen
    if hochfahren:
        logging.info("Go Up")
        if not alterStatusHochfahren:
            alterStatusHochfahren = True
            StartzeitBewegung = now()
        runterfahren = False
        GPIO.output(PIN_RELAIS_DOWN, RELAISOFF)
        time.sleep(0.2)
        GPIO.output(PIN_RELAIS_UP, RELAISON)
    elif runterfahren:
        logging.info("Go Down")
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
    	    logging.info("stop")
        stop = False
        GPIO.output(PIN_RELAIS_DOWN, RELAISOFF)
        GPIO.output(PIN_RELAIS_UP, RELAISOFF)
        hochfahren = False
        runterfahren = False
        buttonsLocked = True
    else:
        alterStatusStop = False

    if (hochfahren == True or runterfahren == True) and mynow - StartzeitBewegung > 1.0/60.0 /60.0 *80.0: # nach 20 Sekunden schaltet sich rauf/runter selber ab.
        logging.info("BewegungsMaxTimeout -> bewegung sicher schon fertig")
        stop = True
