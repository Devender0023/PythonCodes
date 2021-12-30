expense = {
			"January":2200, 
			"February": 2350, 
			"March": 2000, 
			"April":2130, 
			"May":2190
			}

print(expense["February"] - expense["January"])
print(expense["January"] + expense["February"] + expense["March"])


for i in expense:
	if expense[i] == 2000:
		print(i)
		break 



