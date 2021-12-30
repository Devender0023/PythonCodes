def get_multiples(number = 1):
    i = 1
    while True:
        yield number * i
        i+=1


evens = get_multiples(2)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))