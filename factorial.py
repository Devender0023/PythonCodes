def factorial(num):
	sum = 1
	for i in range(1, num+1):
		sum = sum*i
	yield sum
	#print(sum)

factorial(5)