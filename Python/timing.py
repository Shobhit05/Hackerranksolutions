import string
import calendar
from datetime import datetime
##date=datetime.date.today()
a,b,c=raw_input().split()
d=[a,b,c]
date="-".join(d)
date2=datetime.strptime(date , '%m-%d-%Y').date()
day=calendar.day_name[date2.weekday()]
print string.upper(day)
