import datetime
from Sun import Sun


def now ():
    """returns the current time in floated hours. 11.5000 means 11 hours, 30 Minutes """
    mynow = datetime.datetime.utcnow().time()
    output = 0.0 + mynow.hour +(0.0 +  mynow.minute)/60 + (0.0 + mynow.second)/3600
    # print "now-time: " + str(output)
    return output


#Use GPS Coordinats for morning open and evening close
COORDS = {'longitude' : 11.581981, 'latitude' : 48.135125}
SUN = Sun()

mynow =  now()
sunrise = SUN.getSunriseTime(COORDS)['decimal']
sunset = SUN.getSunsetTime(COORDS)['decimal']
print sunrise
print sunset
print mynow