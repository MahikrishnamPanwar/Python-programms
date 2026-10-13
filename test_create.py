
import pymysql

connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'root',db = 'mindcoders2')

cursor = connection.cursor()

sql = """
CREATE TABLE emp (
      id INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(100) NOT NULL,
      age INT,
      city VARCHAR(50)
);
"""

cursor.execute(sql)
connection.commit()
connection.close()

print("Table created successfully")
