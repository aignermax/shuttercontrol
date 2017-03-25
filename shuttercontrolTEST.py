import datetime
import time
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

def timeZoneOffset():
    """returns the difference of the timezone and UTC also considering summer time"""
    is_dst = time.daylight and time.localtime().tm_isdst > 0
    utc_offset = - (time.altzone if is_dst else time.timezone)
    return utc_offset /60/60

print "time offset: " + str(now() + timeZoneOffset())
print sunrise
print sunset
print mynow
