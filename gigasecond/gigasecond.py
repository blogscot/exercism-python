import datetime


def add_gigasecond(birthday):
    gigasecond = datetime.timedelta(seconds=1000000000)
    return birthday + gigasecond
