import re
text="The Sunday Afternoon"
#result= re.match(r"T", text)
#result=re.match(r"t", text, flags=re.IGNORECASE)
#result=re.match(r"t.", text, flags=re.IGNORECASE)
#result=re.match(r"t.*", text, flags=re.IGNORECASE)
result=re.match(r"t.*?noon", text, flags=re.IGNORECASE)
if result is None:
	print("No match");
else:
	print(result.group())

#re.match(r"o.*?", text, flags=re.IGNORECASE)