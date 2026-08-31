#Class Attributes
#kind of static vars like java

class Machine:
	count=0
	
	def __init__(self):
		Machine.count+=1

Machine()
Machine()
print(Machine.count)