from sqlite3 import *

conn=connect('users.db')

cur=conn.cursor()


cur.execute('''CREATE TABLE users(name text,gender text,age text ,email text,password text)''')



conn.commit()
conn.close()

