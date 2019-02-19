import MySQLdb

def connection():
    conn = MySQLdb.connect(
            host="localhost",
            user="forethought",
            passwd="123456",
            db=""
    )
