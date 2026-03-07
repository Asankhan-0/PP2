def dbl(m):
    d = m.group()
    return d*2

import re
t = input()
res = re.sub(r"\d", dbl, t)
print(res)