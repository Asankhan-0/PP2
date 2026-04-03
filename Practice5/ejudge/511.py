import re
txt = input()
let = re.findall(r"[A-Z]", txt)
print(len(let))