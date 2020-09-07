import pymysql


db = pymysql.connect('localhost', 'root', '000000', 'data')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS zb1")

zb = """CREATE TABLE zb1 (
         frame_num  CHAR(20),
         people_num CHAR(20),
         x  float(32),
         y  float(32))"""

cursor.execute(zb)

db.close()


