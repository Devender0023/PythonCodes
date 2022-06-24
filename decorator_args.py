from functools import wraps
from time import sleep


def delay(val):
	def wait(fn):
		@wraps(fn)
		def wrapper(*args,**kwargs):
			print(f"Waiting {val}s before running {fn.__name__}")
			sleep(val)
			fn(*args,**kwargs)
		return wrapper
	return wait


@delay(4)
def say_hi():
	print("hi")

say_hi()