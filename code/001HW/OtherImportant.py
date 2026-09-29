#1 Use end parameter if you dont want a new line
print("Hello Dear,", end=" ") #Add space so that next word has a space seperation
print("How do you do?") #Hello Dear,  How do you do?

#2 Print Numbers and text
print('I am a', 35, "years old guy.")

#3 Multiline comments Trick
"""
This is treated like a multiline comment since no variable is assigned to this string
As long as the string is not assigned to a variable, Python will read the code, 
but then ignore it, and you have made a multiline comment.
"""
print("Above is a good way to make a multiline comment")

#4 You can assign multiple variable in one line
#Make sure the number of variables matches the number of values, or else you will get an error.
x, y, z = "Orange", "Banana", "Cherry"
print(x, end=", ")
print(y, end=", ")
print(z)

#5 Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to 
# extract the values into variables. This is called unpacking.
fruits = ["aam", "anaar", "seb"]
x, y, z = fruits #Unpacking
print(x, end=", ")
print(y, end=", ")
print(z)

#6 Global Vars: All variable outside of function are global variables
# You can use global keyword to create 
# You shouldn't use global variables.
def my_func():
    global awes # seperate declaration
    awes="awesome"
my_func() # calling this is mandatory 
print("python is", awes)

#7 Setting the Specific Data Type
# If you want to specify the data type, you can use the following type constructor functions
x = str("Hello World")

#8 Casting to different types
x=1
a=float(x)
b=str(x)
print(a,b)