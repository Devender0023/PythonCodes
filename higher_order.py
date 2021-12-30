def sum(n, func):
	total = 0
	for num in range(n):
		total += func(num)
	return total

def square(x):
	return x*x



count = int(input("Enter the number: "))
print(sum(count, square))