class Person:
    def __init__(self, name):
        self._name=name
    def __str__(self):
        return f"Hello I am {self._name}"
    def __repr__(self):
        return f'Person("{self._name}")'
p=Person("Tom")

print(repr(p))

text = repr(p)
print(eval(text))