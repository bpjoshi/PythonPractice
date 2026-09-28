value=1
while value < 5:
    if value == 2:
        print("Not prinring 2")
        value+=1
        continue
    else:
        print("current value: ", value)
    value+=1
else:
    print("The while loop is now finished") 
    # only prints if while loop was not using break or exception