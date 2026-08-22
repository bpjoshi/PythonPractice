days = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}


print(days.pop("sun"))
print(days.popitem());
print(days)

del days["mon"]
print(days)

keys=days.keys()
values=days.values()
items=days.items()

print(type(keys))
print(type(values))
print(type(items))