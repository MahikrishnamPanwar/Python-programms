
import pymysql

connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'root',db = 'mindcoders2')

cursor = connection.cursor()

sql = "select * from emp"

cursor.execute(sql)

result = cursor.fetchall()

# print(type(result))
# print(result)

for data in result:
    print(data[0],'\t',data[1],'\t',data[2],'\t',data[3])

connection.commit()
connection.close()
