import re
text="ID: 123 Some Corp. Serial: 345"

#result= re.match(r".*?\d{3}", text)
result=re.match(r".*(\d{3})", text)
if result is None:
    print("No match")
else:
    print(result.group(1))