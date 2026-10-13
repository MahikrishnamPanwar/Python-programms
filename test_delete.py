
import pymysql

connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'root',db = 'mindcoders2')

cursor = connection.cursor()

sql = "DELETE from emp where id = 2"

cursor.execute(sql)
connection.commit()
connection.close()

print("Record has been deleted")
