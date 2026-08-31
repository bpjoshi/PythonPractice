class Machine:
    def __init__(self):
        print("machine constructor")
class Car(Machine):
    def __init__(self):
        #super().__init__()
        print("car constructor")

car= Car()