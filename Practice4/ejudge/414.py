from datetime import datetime

a = input().split()
b = input().split()

d1 = datetime.strptime(a[0], "%Y-%m-%d")
d2 = datetime.strptime(b[0], "%Y-%m-%d")

if a[1][3]=='+':
    sign1 = 1
        else:
            sign1 = -1
if b[1][3]=='+':
    sign2 = 1
        else:
            sign2 = -1

sec1=int(d1.timestamp())-sign1*(int(a[1][4:6])*3600 + int(a[1][7:9])*60)
sec2 =int(d2.timestamp())-sign2*(int(b[1][4:6])*3600 + int(b[1][7:9])*60)

print(abs(sec1-sec2)//86400)