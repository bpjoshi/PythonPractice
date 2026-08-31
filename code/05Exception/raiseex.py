class MyException(Exception):
	pass

try:
      raise MyException("oh no!")
except Exception as ex:
       print(ex)
       print(type(ex))