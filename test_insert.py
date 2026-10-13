
import pymysql

connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'root',db = 'mindcoders2')

cursor = connection.cursor()

sql = """INSERT INTO emp (id,name,age,city) VALUES(1,'shankar',15,'delhi'),(2,'sheetal',18,'noida'); """

cursor.execute(sql)
connection.commit()
connection.close()

print("Values inserted in emp table")
