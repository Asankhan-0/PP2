import re
txt = input()
nums = re.findall(r"\d{2,}", txt)
print(" ".join(nums))