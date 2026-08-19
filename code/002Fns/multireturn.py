def names():
	#dont have to be same type
	#return "Bob", 1, "Pete" - this works fine
    return "Bob", 1, "Pete"
#can retrieve values like this
name1, name2, name3=names()
print(name1,name2, name3)
#Type is tuple
print(type(names()))