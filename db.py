import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud_python'
)

cursor = connection.cursor()
