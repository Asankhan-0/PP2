import re

t = input()
p = input()
t1 = re.split(p, t)
print(",".join(t1))