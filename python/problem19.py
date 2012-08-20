#0 is monday

day = 0
sundays = 0

for year in range(1900, 2001):
    for month in range(0, 12):
        if month == 1 and year > 1900 and year % 4 == 0:
            days = 29
        elif month == 1 and year > 1900 and year % 4 != 0:
            days = 28
        elif month == 1 and year == 1900:
            days = 28
        elif month in [3, 5, 8, 10]:
            days = 30
        else:
            days = 31
        
        day = day + days
        if year > 1900 and day % 7 == 6:
            sundays = sundays + 1

print sundays
