class User():
	def __init__(self,first,last,age):
		self.name = first
		self.last = last
		self.age = age


user1 = User("Dev", "Kumar", 22)
user2 = User("Shikha", "Sharma", 22)
user3 = User("Bada", "Billu", 2)

print(user1.name, user1.last, user1.age)
print(user2.name, user2.last, user2.age)
print(user3.name, user3.last, user3.age)


