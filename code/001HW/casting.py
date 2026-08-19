#We are calculating how many dozen of bananas we can make
value=input("Enter number of bananas available> ")
print("total bananas: ", value)
dozens=int(value)//12 # / for float division and // for int division
print("Dozens you can make: "+ str(dozens))