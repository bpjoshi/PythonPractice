raining=False
temp=25

if temp>27 and not raining:
    print("dry hot weather")
elif temp>27:
    print("hot and humid")
else:
    print("cold weather")

action="go walk" if not raining else "stay indoor"
print("what should i do?: "+action)