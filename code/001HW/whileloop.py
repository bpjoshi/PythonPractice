value=1
while value < 10:
    print("1st-print", value)
    if value == 2:
        value+=1
        print("====lb==")
        continue
    else:
        print("I am not 2")
    print("====lb==")
    value+=1
else:
    print("The while loop is now finished") 
    # only prints if while loop was not using break or exception