import re
tag =r'<div id="123">Hello</div>'
#can use single quote with double and vice versa

# result=re.match(r"""
# 						<div\s+#Match opening tag
# id="(d+)" #Match Id
# > # closing tag bracket
# ([^<>]+) #get content between open and close tag
# </div>

# 					""", tag, re.VERBOSE)
tag =r'<div id="123">Hello</div>'
result= re.match(
    r"""
        <div\s+ #Initial div with space
        id="(\d+)" #match id
        > #closing tag
        ([^<>]+) #Match one or more of anything not < and >
        </div>
    """, tag, re.VERBOSE)
print("No match" if result is None else result.groups())