import re

t = input()
p = input()
lett = re.escape(p)
num = re.findall(lett, t)
print(len(num))