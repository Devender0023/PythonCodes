
with open("alice.txt") as f:
	lines = f.read()

with open("alice.txt", "w") as f1:
	f1.write(lines.replace("Alice", "Colt"))	
 #    		'words':sum(len(line.split()) for line in content),
 #    		'characters':sum(len(line) for line in content)
 #    }
	# print(dict1)