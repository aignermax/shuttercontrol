import datetime
from Sun import Sun


def now ():
    mynow = datetime.datetime.utcnow().time()
    return 0.0 + mynow.hour + mynow.minute/60 + mynow.second/3600


#Use GPS Coordinats for morning open and evening close
COORDS = {'longitude' : 11.581981, 'latitude' : 48.135125}
SUN = Sun()

mynow =  now()
sunrise = SUN.getSunriseTime(COORDS)['decimal']
sunset = SUN.getSunsetTime(COORDS)['decimal']
print sunrise
print sunset
print mynow