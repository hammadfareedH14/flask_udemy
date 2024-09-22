import sqlite3  # # Import the sqlite3 library to work with SQLite databases

connection = sqlite3.connect('data.db') # Establish a connection to the SQLite database
cursor = connection.cursor() # Create a cursor object using the connection to execute SQL commands
create_table = "CREATE TABLE users(id int, username text, password text)" # SQL command to create a table named 'users',
cursor.execute(create_table) # Execute the SQL command to create the 'users' table

user = (1, 'jose', 'asdf') # user record as a tuple with values for 'id', 'username', and 'password'
insert_query = "INSERT INTO users VALUES(?,?,?)" # SQL command to insert a user record into the 'users' table
cursor.execute(insert_query, user) # Execute the SQL command to insert the single user record into the 'users' table
users = [   # multiple user records as a list of tuples
    (2, 'rolf', 'fdsa'),
    (3, 'anne', 'xyz')
]

cursor.executemany(insert_query, users) # SQL command to insert multiple user records into the 'users' table

select_query = "SELECT * FROM users" # SQL command to select all records from the 'users' table
for row in cursor.execute(select_query): # Iterate over the result set and print each row
    print(select_query)
connection.commit() # Commit the current transaction to the database to save all changes
connection.close()  # Close the connection to the database

# SQL:
        # CREATE: The statement is used to create a new table, database, index, or other objects in the database.
        # INSERT: The statement is used to add new rows of data to a table.
        # SELECT: The statement is used to retrieve data from a database.
        # UPDATE: The statement is used to modify existing records in a table.
        # TABLE:  The keyword is used to specify the table to create, modify, or interact with in the database. 
        # INTO:   The keyword is used in conjunction(connect) with INSERT to specify the table to insert data into. 
        # VALUES: The keyword is used in the INSERT statement to specify the data to be inserted into the columns of the table. 
        # FROM:   The keyword is used in the SELECT statement to specify the table from which to retrieve the data.   
        # WHERE:  The clause is used to filter records that meet a specific condition.
        # SET:    The clause specifies the columns and the new values that will be assigned to them.