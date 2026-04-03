import re
txt = input()
words = re.findall(r"\w+", txt)
print(len(words))