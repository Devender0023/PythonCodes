def interleave(s1, s2):
	return ''.join(''.join(x) for x in (zip(s1, s2)))


print(interleave('hi', 'ha'))


def triple_and_filter(nums):
    return list(num*3 for num in filter(lambda num: num%4==0, nums))

print(triple_and_filter([6, 8, 10, 12]))
print(triple_and_filter([1, 2, 3, 4]))


def extract_full_name(collection):
	return list(map(lambda val : f"{val['first']} {val['last']}", collection))

print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))
