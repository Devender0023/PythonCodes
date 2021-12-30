def sum_all_nums(*args):
	print(args)
	total = 0
	for num in args:
		total += num 
	return total

print(sum_all_nums(6, 6, 5, 7, 4, 6, 7))
print(sum_all_nums(*[1, 2, 3, 4, 5, 6]))