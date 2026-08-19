# tuple functions and methods

numbertuple=7,2,7,4,9,5,4
print(numbertuple)
print(len(numbertuple))
print(min(numbertuple))
print(max(numbertuple))
print(numbertuple.count(4)) #num of occurences of 4
print(numbertuple.index(4)) # return index of first 4 in the tuple

# print(numbertuple.index(6)) - ValueError: tuple.index(x): x not in tuple

# Above works with string too

text="it_was_the_best_timez"

print(text)
print(len(text))
print(min(text)) # _
print(max(text)) # z
print(text.count("w")) # 1
print(text.index("w")) #3
