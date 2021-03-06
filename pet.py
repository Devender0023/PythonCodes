class Pet:
	allowed = ["cat", 'dog', 'fish', 'rat']
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species
	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog") 

print(cat.species)
cat.set_species("rat")
print(cat.species)
Pet.allowed.append("tiger")
print(cat.allowed)
