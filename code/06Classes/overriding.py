class Animal:
	def speak(self):
		print("I am an animal")

class Cat(Animal):
	def speak(self):
		print("meeouw")

cat = Cat()
cat.speak()