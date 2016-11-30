__author__ = 'Zane'

import MySQLdb

def db_conn():
    DB_PATH = "localhost"
    DB_USER = "root"
    DB_NAME = "book_recommendation"
    DB_PASS = "123456"
    conn = MySQLdb.connect(DB_PATH, DB_USER, DB_PASS, DB_NAME)
    return conn

def db_select(sql, conn):
    cursor = conn.cursor()
    try:
    	cursor.execute(sql)
    	result = cursor.fetchall()
    	return result
    except:
    	print "[ERROR]: CANNOT fecth data"

def db_insert(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def db_update(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def db_close(conn):
    conn.close()

#if __name__ == '__main__':
#	conn = db_conn()
#	result = db_select("SELECT * FROM `bx-users`;", conn)#
#	if result != None:
#		print result
#	conn.close()