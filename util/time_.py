import calendar
import datetime

from dateutil import tz

def utcnow():
    return datetime.datetime.now(tz.tzutc())

def current_timestamp():
    return calendar.timegm(utcnow().timetuple())
