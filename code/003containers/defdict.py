#import a module
from collections import defaultdict

people={
    "Bob":42,
    "Sue":44,
    "Steve":25
}

print(people.get("Ethel", 99)) #default value

days=defaultdict(str) #type of values
days.update({"mon": "Monday"})

print(days) #you also get defualt class

print(days["wed"]) #It doesn't throw trace back error like it would in normal case
#that's why use defaultdict

