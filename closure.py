from random import choice

def make_laugh_at_func(person):
	def get_laugh():
		laugh = choice(('HAHAHAHA', 'lol', 'thehehhe'))
		return f"{laugh} {person}"

	return get_laugh

laugh_at = make_laugh_at_func("Billu")

print(laugh_at())
print(laugh_at())