import pymysql

connection = pymysql.connect(
    host='den1.mysql6.gear.host',
    user='crudpython',
    password='Vy7KD6_~0x7i',
    db='crudPython'
)

cursor = connection.cursor()


def create_table():
    sql = "CREATE TABLE IF NOT EXISTS contact (names VARCHAR(100), surnames VARCHAR(100), phones BIGINT, emails VARCHAR(100));"
    cursor.execute(sql)
