from datetime import datetime, timedelta

def to_utc(date_s):
    d, tz =date_s.split()
    dt=datetime.strptime(d, "%Y-%m-%d")
    sign=1 if tz[3] == '+' else -1
    hours=int(tz[4:6])
    mins = int(tz[7:9])
    offset=timedelta(hours=hours, minutes=mins) * sign
    return dt - offset

b = to_utc(input())
now = to_utc(input())
bday = b.replace(year=now.year)
if bday.month == 2 and bday.day == 29:
    try:
        bday = bday
    except ValueError:
        bday = bday.replace(day=28)

if bday < now:
    bday = bday.replace(year=now.year + 1)
    if bday.month == 2 and bday.day == 29:
        try:
            bday = bday
        except ValueError:
            bday = bday.replace(day=28)
diff_sec = (bday - now).total_seconds()

diff_days = int(diff_sec // 86400)

if diff_sec % 86400 > 0:
    diff_days += 1

print(diff_days)