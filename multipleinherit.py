class A:
	def do_something(self):
		print("Method defined in : A")

class B(A):

	def do_something(self):
		print("Method defined in : B")

class C(A):

	def do_something(self):
		print("Method defined in : C")

class D(B, C):

	def do_something(self):
		print("Method defined in : D")


help(D)
