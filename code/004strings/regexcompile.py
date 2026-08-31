import re
text="dog cat mouse"

compiledRegex=re.compile("C.*t", flags=re.I); #re.I= IGNORECASE
#flags have to be compiled too
#you can't use flags, if you have not compiled them 

result=re.sub(compiledRegex, "girraffe", text)
print(result)
print(text)
