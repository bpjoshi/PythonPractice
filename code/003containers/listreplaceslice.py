#TypeError: list() takes at most 1 argument (7 given)
#commented line doesn't work because list() expects only 1 argument a tuple or other container
#numbers=list(0,1,2,3,4,5,6,7)
numbers=list((0,1,2,3,4,5,6,7))
numbers[2:4]=(0,0,0,0) 
print(numbers) #[0, 1, 0, 0, 0, 0, 4, 5, 6, 7]

numbers[2:6] =[] #replace 2,3,4,5 indexes with empty list
print(numbers) #[0, 1, 4, 5, 6, 7]

print(numbers[1::2]) #you can't do random replacement ..you need exact 3 values
numbers[1::2]=["Hello", "to", "you"]
print(numbers)