fruits = ["apple", "banana"]
#1 Adding item with append()
fruits.append("mango")
print(fruits)

#2 insert item at particular position
fruits.insert(1, "cheeku")
print(fruits)

#3 Removing item using remove()
fruits.remove("cheeku") # ValueError: list.remove(x): x not in list on doing remove("kela")
print(fruits)

#4 removing item using pop() by index
fruits.pop(1) # IndexError: pop index out of range for removing values out of range
print(fruits)

#5 len() 
print(len(fruits))

#6 Loop through
for fruit in fruits:
	print(fruit)

#7 Check if Item exists
print("banana" in fruits)

#8 slicing [start: end] 

#9 Common Beginner methods
nums=[4,2,8,1]
print("Orginal: ", nums, end=", ")
nums.sort()
print("sort: ", nums, end=", ")
nums.reverse()
print("reverse: ", nums, end=", ")
print("number of 2's: ", nums.count(2), end=", ")
print("index of 8: ", nums.index(8))

del nums[0] #del keywords deletes
print(nums)
nums.pop() #removes last item if index not provided
print(nums)
# del nums #deletes entire list # NameError: name 'nums' is not defined

nums.clear() # clears content
print(nums)

#Using index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
	print(i+1, ". ", thislist[i])

#while loop
i=0; 
while i<len(thislist):
	print(i, end=", ")
	i+=1
else:
	print("\n")

#List comprehension
[print(x) for x in thislist] #what sorcery is this

squares = [x * x for x in range(1,10,2)] #List comprehension is used for producing lists
print(squares)

#Sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

#Customize sort function
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# sort the list of names based on name length
name_list=["Bob", "Tom", "Alexander", "Ryan", "Josh"]
name_list.sort(key=len)
print(name_list)
#sort names alphabetically
name_list.sort(key=str)
print(name_list)

## Make a copy of a list
list1=name_list.copy()
list2=list(list1)
list3=list2[:]

print(name_list==list1)
print(list1==list3)

## join 2 lists
# list1+list2
#List1.extend(list2)
#for x in list2: list1.append(x)