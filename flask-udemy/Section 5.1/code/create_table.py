# module
import sqlite3

connection = sqlite3.connect("data.db") # established database connection
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # create users if not exxist
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS items (username text, price real)" # create a items table if not exsists.
cursor.execute(create_table)
connection.commit()
connection.close()