#MultipleInheriteance

class Car:
	def start(self):
		print("car starting")

class Alarm:
	def on(self):
		print("alarm on")

class SafeCar(Car, Alarm):
	pass

s=SafeCar()
s.start()
s.on()