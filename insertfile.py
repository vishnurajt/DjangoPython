import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)
cursor = db.cursor()
f=open("sqltext.txt","r")
for lines in f:
    datas=lines.rstrip("\n").split(",")
    # lstr=datas.split(",")
    #print(lstr[1])
    sql="insert into employeee values(%s,%s,%s,%s)"
    # record=(lstr[0],lstr[1],lstr[2],lstr[3])
    cursor.execute(sql,datas)
    db.commit()
db.close()



