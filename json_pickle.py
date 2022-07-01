import jsonpickle

class Cat:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f'Hi, My name is {self.name} and I am a {self.breed} cat.'


c = Cat('Billu', 'Taby')

# with open('cat.json', 'w') as file:
#     store = jsonpickle.encode(c)
#     file.write(store)

with open('cat.json', 'r') as file:
    data = file.read()
    cat = jsonpickle.decode(data)
    print(cat)



