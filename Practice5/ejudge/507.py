import re

t = input()       
p = input()    
replace = input()
result = re.sub(re.escape(p), replace, t)
print(result)