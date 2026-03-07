import re

t = input()
w = re.findall(r"\b[A-Za-z]{3}\b", t)
print(len(w))