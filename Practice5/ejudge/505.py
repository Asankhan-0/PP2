import re

txt = input()
x = re.search(r"[A-Za-z]\d", txt)
print("Yes") if x else print("No")