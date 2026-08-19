def calculaty_area():
    pass #temporarily make it compile
def cal_area(length, width=1, height=1):
    #default value parameters need to be towards the end
    #if widht=1, height=1, length order is like this then program wont work
    return length*width*height

myArea=cal_area(10,15)
print("The area is ", myArea)

#you can call in random order if you specify param names
another_area=cal_area(height=10, length=2, width=5)
print(another_area)

#The ones you dont want to do param names ..have to go in order 
new_area=cal_area(10, height=5, width=4)
print(new_area)