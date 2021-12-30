# import pdb 
# first = 'First'
# second = 'Second'
# pdb.set_trace()
# result = first+second
# third = 'Third'
# result += third
# print(result)

# def add_numbers(a, b, c, d):
# 	import pdb; pdb.set_trace()

# 	return a+b+c+d

# print(add_numbers(1, 2, 3, 4))

def divide(num1, num2):
	total = 0
	try: 
		total = num1/num2
	except TypeError:
		print("Please provide two integers or floats")
	except ZeroDivisionError:
		print("Please do not divide by zero")
	return total


print(divide(4, 2))
print(divide([], '1'))
print(divide(1, 0))
