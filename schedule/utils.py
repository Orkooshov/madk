import datetime as dt
from .models import Weekday, Week


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['weekday_today'] = get_weekday_today()
        context['weekday_tomorrow'] = get_weekday_tomorrow()
        context['week'] = get_week()
        return context


def get_weekday_today() -> str:
    '''Gets the weekday of today'''
    today_date = dt.datetime.today()
    weekday_index = today_date.weekday()
    return Weekday.labels[weekday_index]


def get_weekday_tomorrow() -> str:
    '''Gets the weekday of tomorrow'''
    tomorrow_date = dt.datetime.today() + dt.timedelta(days=1)
    weekday_index = tomorrow_date.weekday()
    return Weekday.labels[weekday_index]

def get_week() -> Week:
    '''Gets the week number (first or second)'''
    week_num = dt.date.today().isocalendar().week
    return Week(week_num % 2 + 1)