import csv

def update_users(old_f_name, old_l_name, new_f_name, new_l_name):
    with open('users.csv') as file:
        data = csv.reader(file)
        users = list(data)
    count = 0
    with open('users.csv', 'w') as file:
        writer = csv.writer(file)

        for user in users:
            if user[0] == old_f_name and user[1] == old_l_name:
                writer.writerow([new_f_name, new_l_name])
                count+=1
            else:
                writer.writerow(user)


    return f'Users updated: {count}'

print(update_users("Colt", "Steele", "Dev", "Kumar"))



