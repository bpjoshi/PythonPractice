print("Do you wnat to know - what should you do?")
raining = input("Is it raining? (True/False) > ").strip().lower() == "true"
#.strip().lower() == "true" is done to convert string to boolean
temp = float(input("What is the temperature in Celsius? > "))
#float to change temperature from String value
#raining=False

if temp>27 and not raining:
    print("dry hot weather")
elif temp>27:
    print("hot and humid")
else:
    print("cold weather")

action="go walk" if not raining else "stay indoor"
actionString="you should "

print(actionString+action)