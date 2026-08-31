class Person:
    def __init__(self, name):
        self._name=name
    def __str__(self):
        return f"Hello I am {self._name}"
    def __repr__(self):
        return f'Person("{self._name}")'
    def eating(self, item):
        return "I am eating "+item
class Employee(Person):
    def on_vacation_mode(self):
        return "I am on holiday"

e=Employee("Sue")
print(e.eating("samosa"))
print(e.on_vacation_mode())