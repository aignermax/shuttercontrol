
import datetime
from Sun import Sun

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