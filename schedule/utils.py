import datetime as dt
from .models import Schedule

weekdays = Schedule.Weekday.labels # ['Понедельник', ...]

def get_weekday_today() -> str:
    '''Gets the weekday of today'''
    weekday_index = dt.datetime.now().weekday()
    return weekdays[weekday_index]

def get_weekday_tomorrow() -> str:
    '''Gets the weekday of tomorrow'''
    weekday_index = dt.datetime.now().weekday() + 1
    return weekdays[weekday_index]