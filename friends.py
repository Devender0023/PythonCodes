import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute sql command
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
c.execute("INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7);")
# commit changes
conn.commit()
conn.close()
