from csv import reader

def find(first, last):
	with open('users.csv') as file:
		users = reader(file)

		for index, user in enumerate(users):
			if first in user and last in user:
				return index
		return 'Not found'

print(find('Alan', 'Turing'))