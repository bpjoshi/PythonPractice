import re
menu ="""
1. Fish
2. Bread
3. Peppers
4. Potatoes
"""
#^ to match start of line and $ to match end of line
result=re.findall(r"^(.*)$", menu, re.MULTILINE)
print(result)