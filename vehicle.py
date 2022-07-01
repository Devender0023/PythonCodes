import pickle

class Vehicle:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'I am a {self.name}'

class Car(Vehicle):

    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels

    def __repr__(self):
        return f'I am a {self.name} that has {self.wheels} wheels and has a roof.'

class MotorCycle(Vehicle):

    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels

    def __repr__(self):
        return f'I am a {self.name} that has {self.wheels} wheels and has no roof.'



bike = MotorCycle('Bike', 2)
car = Car('Car', 4)

vehicle = (bike, car)

with open('Vehicle.pickle', 'wb') as file:
    pickle.dump(vehicle, file)

with open('Vehicle.pickle', 'rb') as file:
    Bike, Car = pickle.load(file)
    print(Bike)
    print(Car)




