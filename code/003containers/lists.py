fruits=["apple", "orange", "grape"]
print(id(fruits))
fruits+=["melon"]
print(id(fruits))
print(fruits)
fruits[0]="strawberry"
print(fruits)
fruits.append("pear") # add single item 
print(fruits)
fruits.extend(["blueberry"]) #add other container list like that this
print(fruits)
fruits.insert(2, "kiwi")
print(fruits)

fruits_tuple=tuple(fruits); #conver to tuple
print(fruits_tuple)
fruits_list=list(fruits_tuple) # convert tuple to list
print(fruits_list)