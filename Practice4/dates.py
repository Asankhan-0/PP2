# Write a Python program to subtract five days from current date.

import datetime
print(datetime.date.today() - datetime.timedelta(5))


# Write a Python program to print yesterday, today, tomorrow.

import datetime
print(datetime.date.today() - datetime.timedelta(1), datetime.date.today(), datetime.date.today()+ datetime.timedelta(1), end=" ")


# Write a Python program to drop microseconds from datetime.

import datetime
print(datetime.now().replace(microsecond=0))


# Write a Python program to calculate two date difference in seconds.

import datetime

d1_str=input()
d2_str=input()
d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d %H:%M:%S")
d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d %H:%M:%S")
diff = d2-d1
diff_sec = diff.days*24*60*60 + diff.seconds
print(diff_sec)



