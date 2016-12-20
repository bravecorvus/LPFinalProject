import pytz
import datetime

start_zone = pytz.timezone('Europe/London')
end_zone = pytz.timezone('Europe/Oslo')
 
start_time = datetime.datetime(2011,5,13,15,0, tzinfo=start_zone)
end_time = datetime.datetime(2011,5,13,19,0, tzinfo=end_zone)

event = gdata.calendar.CalendarEventEntry()
event.when.append(gdata.calendar.When(start_time=start_time.isoformat(), end_time=end_time.isoformat()))