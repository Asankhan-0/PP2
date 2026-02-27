from datetime import datetime, timedelta

s1 = input()
s2 = input()

dt1_str, tz1 = s1.rsplit(' ',1)
dt1 = datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S")
sign1 = 1 if tz1[3]=='+' else -1
h1 = int(tz1[4:6])
m1 = int(tz1[7:9])
dt1_utc = dt1 - timedelta(hours=h1*sign1, minutes=m1*sign1)

dt2_str, tz2 = s2.rsplit(' ',1)
dt2 = datetime.strptime(dt2_str, "%Y-%m-%d %H:%M:%S")
sign2 = 1 if tz2[3]=='+' else -1
h2 = int(tz2[4:6])
m2 = int(tz2[7:9])
dt2_utc = dt2 - timedelta(hours=h2*sign2, minutes=m2*sign2)

print(int((dt2_utc - dt1_utc).total_seconds()))