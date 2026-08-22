#print(hash([1,2,3]))

#TypeError: unhashable type: 'list' ..list are not immutable

print(hash((1,2,3))) # works well

print(hash((1,2,[]))) #doesn't work because this tuple contains empty list which is not immutable