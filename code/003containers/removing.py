numbers=[0,1,2,3,4,5,6]
numbers.remove(4)
print(numbers)

numbers.pop() # last item
print(numbers)
value=numbers.pop(1) #1st index
print(numbers)
print(value)
del numbers[2]
print(numbers)

numbers.clear()
print(numbers)