import re

t = input()
p = re.compile(r"\b\w+\b")
num = p.findall(t)
print(len(num))