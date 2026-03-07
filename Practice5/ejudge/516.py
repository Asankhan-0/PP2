import re
txt = input()
res = re.search(r"Name: (.+), Age: (\d+)", txt)
print(res.group(1), res.group(2))