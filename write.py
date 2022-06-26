
with open("alice.txt") as f:
	content = f.readlines()
	dict1 = {'lines':len(content),
    		'words':sum(len(line.split()) for line in content),
    		'characters':sum(len(line) for line in content)
    }
	print(dict1)