import mysql.connector

database = mysql.connector.connect(
   user = 'root',
   password = 'yourpassword',
   host = 'localhost',
   port = '3306',
   database = 'your_database_name',
   auth_plugin = 'mysql_native_password' #only use this if you are using legacy python or run into an auth_plugin error
   )

cursor = database.cursor()

word = input("Enter a word: ")

cursor.execute("show databases")

for i in cursor:
    print(i)
    
query = cursor.execute("SELECT * FROM student WHERE Expression = '%s'" % word)

results = cursor.fetchall()

if results: 
    print("College", results[1])
else:
    print("no college found!")
