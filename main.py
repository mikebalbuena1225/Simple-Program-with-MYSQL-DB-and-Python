import mysql.connector

database = mysql.connector.connect(
   user = 'root',
   password = '95859585Dr!',
   host = 'localhost',
   port = '3306',
   database = 'aiore_tool_kit',
   auth_plugin = 'mysql_native_password'
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