months = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}


print(months["jan"])
months["apr"]="Avril"
print(months)

months.update({"feb": "Fevrier"})
print(months)

for mon in months:
    print(mon, months[mon])

for mon in months.values():
    print(mon)

for mon in months.items():
    print(mon)
#above prints like below tuples
#('nov', 'November')
#('dec', 'December')
#unpacking the tuple
for monAbrv, name in months.items():
    print(monAbrv, name)

print("jan" in months)

print("JAN" in months)
