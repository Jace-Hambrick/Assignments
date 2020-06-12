import sqlite3

# Making a new DB and then connecting to it
# Adding columns and values

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
query = 'DROP TABLE demo'
curs.execute(query)
query = 'CREATE TABLE demo (s varchar(255), x varchar(255), y varchar(255));'
curs.execute(query)
query = "INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);"
curs.execute(query)
query = "INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);"
curs.execute(query)
query = "INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);"
curs.execute(query)
conn.commit()

print("The db demo_data has been made and populated with table 'demo' and values.")

query = "SELECT COUNT (*) FROM demo"
result = curs.execute(query).fetchall()
print("There are", result[0][0], "rows in the table 'demo'.")

query = "SELECT COUNT (DISTINCT x >= 5 AND y >= 5) FROM demo;"
result = curs.execute(query).fetchall()
print("There are", result[0][0], "rows where both x and y have values greater than or equal to 5.")

query = "SELECT COUNT (DISTINCT y) FROM demo;"
result = curs.execute(query).fetchall()
print("The y column has", result[0][0], "unique values.")