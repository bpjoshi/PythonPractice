#1 Modify the strings
a="Hello World"
print("1." , a.upper(), end=", ")
print("2." , a.lower(), end=", ")
print("3." , " The Himalayas are great   ".strip(), end=", ")
print("4.", a.replace("Hello", "Bonjour"), end="\n")
print("5.", "Hello, Wolrd, Bonjour, A tous".split(","))

#2 Formatting Strings
"""
age = 36
#This will produce an error: we cannot combine strings and numbers like this
txt = "My name is John, I am " + age
print(txt)
"""
#But we can combine strings and numbers by using f-strings or the format() method!
#f-Strings
name,age="bhagwati", 35
print(f"My name is {name} and I am {age}.")
print(f"My name in capital is: {name.upper()}")
p = 10; q = 20
print(f"Sum = {p + q}")

#format method
print("My name is {} and I am {} years old.".format(name.upper(), age))
print("{1} {0}".format("World", "Hello")) #Positional argument

#Named Argument
print("Name: {name}, Age: {age}".format(name="Bhagwati",age=30))

#Number formatting
# .2f -> float with 2 decimal places
price = 123.45678
print(f"The price is: {price:.2f}")

#Comma Seperator
num=12345678
print(f"{num:,}")

#Percentage
value = 0.8532
print(f"{value:.2%}")

#Width and alighment
print(f"|{name:>10}|"); #right
print(f"|{name:<10}|"); #left
print(f"|{name:^10}|"); #center

#Padding
num=25
print(f"the num is: {num:05}")