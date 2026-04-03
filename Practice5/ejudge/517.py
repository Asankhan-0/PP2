import re
txt = input()
date = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", txt)
print(len(date))