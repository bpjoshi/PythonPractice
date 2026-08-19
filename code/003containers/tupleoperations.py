# operators with tuples
fruits1="Apple","banana"
fruits2="mango", "pear"
print(fruits1+fruits2) #<mix of 2 tuples

print(fruits1*3) #- 3 replication
print(id(fruits1)) 
fruits1+=fruits2
# tuples are immutable ..must have diff ids
print(fruits1)
print(id(fruits1)) #different than line 7

