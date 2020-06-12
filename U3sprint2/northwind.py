import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
query = "SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;"
print("The ten most expensive items per unit price are", curs.execute(query).fetchall(), ", in descending order.")

query = "SELECT ROUND(AVG(HireDate - BirthDate)) FROM Employee"
result = curs.execute(query).fetchall()
print("The average age of an employee at the time of hire is", result[0][0])

query = "SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName FROM Product INNER JOIN Supplier ON Product.SupplierId=Supplier.Id ORDER BY UnitPrice DESC LIMIT 10;"
result = curs.execute(query).fetchall()
print("The ten most expensive items per unit price are", curs.execute(query).fetchall(), "in descending order. This includes the Company Name.")

query = "SELECT CategoryName, Product.CategoryId, COUNT(*) NumberCount FROM Product INNER JOIN Category ON Product.CategoryId=Category.Id;"
result = curs.execute(query).fetchall()
print("The largest Category is Beverages, as shown ", curs.execute(query).fetchall(), "CategoryName, CategoryID, NumberCount")













