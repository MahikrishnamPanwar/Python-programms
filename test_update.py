
import pymysql

connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'root',db = 'mindcoders2')

cursor = connection.cursor()

sql = "UPDATE emp SET age = 26,city = 'indore' where id = 1"

cursor.execute(sql)
connection.commit()
connection.close()

print("Record has been updated")

