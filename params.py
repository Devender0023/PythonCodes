num = int(input("Enter a number to square it: "))
def square_of_number(num):
	return num**2

print(square_of_number(num))

def add(a, b):
	return a+b 

def math(a, b, fn = add):
	return fn(a,b)

def subtract(a,b):
	return a-b

print(math(2,2))
print(math(2,2, subtract))

def speak(animal = "dog"):# Define speak below:
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"


print(speak())
print(speak("pig"))

def speak(animal = "dog"):
	noises = {
		"dog" : "woof",
		"pig" : "oink",
		"duck" : "quack",
		"cat": "meow"
	}
	noise = noises.get(animal)
	if noise:
		return noise 
	return "?"

print(speak("duck"))
print(speak("elephant"))







