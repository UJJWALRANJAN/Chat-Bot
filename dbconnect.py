import MySQLdb

def connection():
    conn = MySQLdb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="123456",
            db="thpchat"

    )
    c = conn.cursor()
    return c,conn

c, conn = connection()
