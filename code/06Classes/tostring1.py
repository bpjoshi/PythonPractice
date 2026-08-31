class Person:
    def __init__(self, name):
        self._name=name
    def __str__(self):
        return f"Hello I am {self._name}"

p=Person("Tom")
print(p)

text=str(p)
print(text)