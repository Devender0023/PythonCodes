from csv import reader, writer

with open('addresses.csv') as file:
	csv_reader = reader(file)
	addresses = [[s.upper() for s in row] for row in csv_reader]
	for row in csv_reader:
		print(row)
		
with open('bold_address.csv', 'w') as file2:
	csv_writer = writer(file2)
	for address in addresses:
		csv_writer.writerow(address)