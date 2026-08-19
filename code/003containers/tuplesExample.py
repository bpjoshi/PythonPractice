#Below process is called packing tuple i.e. setting values
#tuples can contain diferent types of values
stuff=("charles", 7, 8.2, True, False , "Cats")
print(stuff)
print(type(stuff))
#tuples are immutable, so below commented line throws exception
#TypeError: 'tuple' object does not support item assignment
#stuff[2]="Leaf"

#unpacking a tuple
name,value1,vlaue2,bool1,bool2, animal=stuff
#full print
print(name,value1,vlaue2,bool1,bool2, animal)
print("---------------seperator------")

#partial read 
person, number1, number, *other=stuff
print(person, number1, number, *other)
print("---------------seperator------")
print("type of *other is list? : ", type(other))
print("---------------seperator------")
#creating a tuple
animals="cat", "dog"

#single tuple can me made with , at the end ..otherwise it will be a string
animal_tuple="cat",
animal_anothertuple=("cat", )
print(animal_tuple)
print(animal_anothertuple)
print("type is ", type(animal_tuple), type(animal_anothertuple))
print("---------------seperator------")