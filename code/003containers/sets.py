numbers={1,3,6,4,4}
print(numbers)
for x in numbers:
    print(x)

numbers.add(7) # add to a set 
print(numbers)

numbers.update([9,8]) #you can add another collection via update method
print(numbers)

numbers.remove(8)
print(numbers)
#numbers.remove(10) unsafe throws exception ..use discard

print.discard(3)
print(numbers)

print.discard(10) #safe