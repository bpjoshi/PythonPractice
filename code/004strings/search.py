import re
text="""
one
two
three
"""
result= re.search(r"t.*e", text, re.DOTALL)
#without re.DOTALL result is only three
print("No match" if result is None else result.group())