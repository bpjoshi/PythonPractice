#1 You can use quotes inside a string, as long as 
# they don't match the quotes surrounding the string:
print('He is called "The Don"')
print("She is not called 'The Don'")

#2 Multi line String - three (double or single) quotes
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

#3 String can be read like arrays but you cannot modify them
# A string in Python is an iterable sequence of characters.
str_arr = "Hello, World!"
print(str_arr[1])
# str_arr[0] = "J" -> TypeError , you can't modify

#4 Looping through a string
for i in "banana":
    print(i, end=", ")
print(" ")

#5 String length : len() function
print(len(str_arr))

#6 Check in string: To check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt) # True

if "free" in txt:
    print("free is present")

if "expensive" not in txt:
    print("expensive is not present")

#7 Slicing a string
b = "Hello, World!"
print(b[2:5]) #llo
print(b[:5]) #Hello -> slice from start
print(b[2:]) #llo, World! -> slice to the end


#8 Negative Indexing: Use negative indexes to start the slice from the end of the string
# Characters: b    a   n   a   n   a
#    Indexes: 0    1   2   3   4   5
# Neg Index: -6   -5  -4  -3  -2  -1
banana_str="banana"
# get the last character
print(banana_str[-1])
#get the second last -> banana_str[-2]
#Check file extension
filename = "report.pdf"
if filename[-4:] == ".pdf":
    print("PDF file")
# Reverse a string
print(banana_str[::-1]) 
# Negative step means python starts from the end of the string
