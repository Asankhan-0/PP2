import re
t = input()
p= re.compile(r"^\d+$")
x = p.search(t)
print("Match") if x else print("No match")