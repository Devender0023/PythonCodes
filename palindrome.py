def is_palindrome(string):
	return string.lower().replace(" ", "") == string[::-1].lower().replace(" ", "")
	
print(is_palindrome("Dad"))


def frequency(list1, search_term):
    return list1.count(search_term)
    

print(frequency([1, 2, 2, 5, 6, 6, 6], 6))


def multiply_even_numbers(collection):
    product = 1
    for num in collection:
        if num%2==0:
            product *= num
    return product

print(multiply_even_numbers([2, 3, 4, 5, 6]))