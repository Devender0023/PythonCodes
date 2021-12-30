midterms = [80, 91, 87]
finals = [85, 76, 83]
students = ["satyam", "shikha", "dev"]

# final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
# print(final_grades)

scores = zip(
	students, 
	map(lambda pair: ((pair[0]+pair[1])/2), zip(midterms, finals))
	)

print(dict(scores))