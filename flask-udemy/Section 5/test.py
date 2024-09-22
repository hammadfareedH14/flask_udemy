# video 4:Import the sqlite3 library to work with SQLite databases
import sqlite3  

# video 4:Establish a connection to the SQLite database named 'data.db',If the database does not exist, it will be created
connection = sqlite3.connect('data.db')

# video 4:Create a cursor object using the connection to execute SQL commands,Call the cursor method to get the cursor object
cursor = connection.cursor() 

# video 4: Define an SQL command to create a table named 'users'
# he table has three columns: 'id' (integer), 'username' (text), and 'password' (text)
create_table = "CREATE TABLE users(id int, username text, password text)"

# video 4: Execute the SQL command to create the 'users' table
cursor.execute(create_table)

# video 4: Define a user record as a tuple with values for 'id', 'username', and 'password'
user = (1, 'jose', 'asdf')

# video 4: Define an SQL command to insert a user record into the 'users' table
insert_query = "INSERT INTO users VALUES(?,?,?)"

# vide 4:Execute the SQL command to insert the single user record into the 'users' table
cursor.execute(insert_query, user)

# video 4: Define multiple user records as a list of tuples
users = [
    (2, 'rolf', 'fdsa'),
    (3, 'anne', 'xyz')
]

# video 4:Execute the SQL command to insert multiple user records into the 'users' table
cursor.executemany(insert_query, users)

# video 4:Define an SQL command to select all records from the 'users' table
select_query = "SELECT * FROM users"

#  video 4:Execute the SQL command to select all records from the 'users' table
# Iterate over the result set and print each row
for row in cursor.execute(select_query):
    print(row)

# video 4:Commit the current transaction to the database to save all changes
connection.commit()

# video 4: Close the connection to the database
connection.close()
