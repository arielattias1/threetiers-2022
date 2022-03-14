import mysql.connector

cnx = mysql.connector.connect(user='root', 
    password='Rh0thm&P0etr9',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

college = input('Enter College name: ')
students = input('Enter Students population: ')

cursor = cnx.cursor()
query = (f'INSERT INTO `Colleges` VALUES (NULL, "{college}","{students}",NULL,NULL,NULL)')

cursor.execute(query)

#print

for row in cursor.fetchall():
    print(row)

cnx.commit()
cursor.close()
cnx.close()


