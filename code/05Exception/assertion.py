value=7
try:
	assert value>8, "oh no"
except AssertionError as a:
	print(a)