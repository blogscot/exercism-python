from datetime import date
import calendar

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

order_list = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4, "last": -1}


def weekdays(offset=0):
    """ A infinite weekday generator """
    day = offset
    while True:
        yield days[day]
        day = (day + 1) % 7


def meetup_day(year, month, day, order):

    month_start, num_days = calendar.monthrange(year, month)
    month_list = zip(range(1, num_days+1), weekdays(month_start))

    day_list = filter(lambda entry: entry[1] == day, month_list)

    if order is "teenth":
        result = filter(lambda x: x[0] in range(13, 20), day_list)[0]
    else:
        result = day_list[order_list.get(order)]

    return date(year, month, result[0])


