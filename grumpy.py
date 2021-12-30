class GrumpyDict(dict):

	def __repr__(self):
		print("None of your business")
		return super().__repr__()

	def __missing__(self, key):
		print(f"You want {key}? Well it aint here!")

	def __setitem__(self, key, value):
		print("UGH! Why you always have to change things.")
		print("Fine! Here is your updated data.")
		super().__setitem__(key, value)


data = GrumpyDict({"first": "Jai", "middle": "Shri", "last": "Ram"})
print(f"{data['first']} {data['middle']} {data['last']}")
data["try"]
data["again"] = "Jai"
print(data)