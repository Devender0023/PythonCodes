def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper

@be_polite # This the syntactic sugar of decorator
def greet():
	print("My name is Billu.")


greet()
