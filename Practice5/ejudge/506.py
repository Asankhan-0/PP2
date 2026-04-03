import re

t = input()

p = r"\S+@\S+\.\S+"

match = re.search(p, t)

if match:
    print(match.group())
else:
    print("No email")