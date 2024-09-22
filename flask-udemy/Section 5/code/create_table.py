# video 6:
import sqlite3

# video 6:
connection = sqlite3.connect("data.db")
# video 6:
cursor =connection.cursor()

# video 6:
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# video 6: excecute a command
cursor.execute(create_table)

#  video 9: create a items table and check if exists or not.
create_table = "CREATE TABLE IF NOT EXISTS items (username text, price real)"
# video 8:execute a commands.
cursor.execute(create_table)
# video 8: insert data into database.
# cursor.execute("INSERT INTO items VALUES ('test'.10.99)")
# video 6: save changes into database. 
connection.commit()
# videdo 6: connection close.
connection.close()