from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time taken: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums():
	return sum(x for x in range(90000000))

@speed_test
def sum_nums1():
	return sum([x for x in range(90000000)])

print(sum_nums())
print(sum_nums1())