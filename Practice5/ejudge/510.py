import re
t = input()
x = re.search(r"cat|dog", t)
print("Yes") if x else print("No")