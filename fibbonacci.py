def fibonacci(num):
	num1 = 0
	num2 = 1
	count = 0

	while count < num:
		yield num1
		#print(num1)
		nth = num1 + num2
		num1 = num2
		num2 = nth
		count += 1

counter = fibonacci(1000000)
print(next(counter))



# def yes_or_no():
#     answer =  "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"

# gen = yes_or_no()
# print(next(gen))
# print(next(gen))


