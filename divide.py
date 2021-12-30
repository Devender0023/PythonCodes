def divide(a, b):
		try:
			result = a/b
		except ZeroDivisionError as err:
			print("Can't divide a number by zero!")
			print(err)
		except TypeError as err1:
			print("a and b must be integers ...")
			print(err1)
		else:
			print(f"{a} divided by {b} is {result}")

print(divide(1, 'a'))
print(divide(344566, 0))