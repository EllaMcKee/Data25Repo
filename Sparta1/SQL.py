import pyodbc as pyodbc

# Details for connection.
server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

# Connect to the database.
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                  + server + ';DATABASE=' + database + ';UID='
                                  + username + ';PWD=' + password)

# Create cursor. Control structure to manage response
cursor = docker_Northwind.cursor()


request = "SELECT * FROM products"

results = cursor.execute(request)

print(results)
