# assignment 
#Walrus operator
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Ternery Operator
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)

#Identity Operators
# The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True
print(x is y) #False # x is not y => True
print(x == y) #True #== Checks if the values of both variables are equal

#Membership
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("Kela" not in fruits)
print("====")
text = "Hello World"
print("H" in text)
print("hello".capitalize() in text)
print("z" not in text)