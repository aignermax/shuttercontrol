from datetime import datetime
import pytz # $ pip install pytz

la = pytz.timezone("Europe/Berlin")
fmt = '%Z%z'
now = datetime.now(la)
now.utcoffset()
now2 = la.localize(datetime.now())
now3 = datetime.now()

print(dir(now))
print(now.utcoffset())
print(now2.strftime(fmt))
print(now3.strftime(fmt))
