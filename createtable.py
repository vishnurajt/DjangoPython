import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)
cursor=db.cursor()
sql="create table employeee(eid varchar(20),name varchar(20),desig varchar(50),salary int)"
cursor.execute(sql)
print("table created")