distance=1.23
height = 2.34

#f string for arguments
#print(f"height: {height}, Distance: {distance}")
#print(f"height: {height:5}, Distance: {distance:10}")

print(f"Height:{height:.1f}, Distance:{distance}")
print("Height:{}, Distance:{}".format(height,distance));
print("Height:{1:.1f}, Distance:{0:.1f}".format(distance,height));
print("Height:,%f Distance:%f" %(height, distance));
print("one\ntwo");
print(r"one\ntwo");