import re
text="az"
result= re.match(r"az", text)
print("No match" if result is None else result.group())

text=r"a\nz" #raw string \n as new line
result= re.match(r"a\\nz", text)
print("No match" if result is None else result.group())
#you have to escape in python 
