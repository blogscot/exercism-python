def weekdays(offset=0):
    day = offset
    while True:
        yield days[day]
        day = (day + 1) % 7


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

l = zip(range(1, 32), weekdays(1))

for i in l:
    print i

print l
