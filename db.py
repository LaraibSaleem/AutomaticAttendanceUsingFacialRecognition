# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:08:43 2020

@author: Laraib
"""



import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb







# --------------- DB_CONNECTION --------------- #
def db_conn():
    try:
        db= MySQLdb.connect("127.0.0.1", "root", "", "AAUFR")
        #print("Connected to db")
    except Exception:
        print("Connection Error")
    return db






# --------------- SIGN_IN --------------- #
def sign_in(p1,p2):
    flag = ""
    conn=db_conn()
    cursor= conn.cursor()
    cursor.execute("select * from user where uname='" + p1 + "' and upass='" + p2 + "'")
    result = cursor.fetchall()
    admintuple = ((1, 'admin', 'admin'),)
    #print(admintuple)
    #print(result)
    if(len(result)==1):
        if(result==admintuple):
            flag = 'admin'
        else:
            flag = 'instructor'
    else:
        print("Invalid credentials")
    conn.close()
    return flag





# --------------- CHECKING_IF_USERNAME_EXISTS --------------- #
def check_uname(p1):
    flag = None
    conn=db_conn()
    cursor= conn.cursor()
    cursor.execute("select * from user where uname='" + p1 + "'")
    result = cursor.fetchall()
    #print(result)
    if not len(result) == 0:
        flag = True
        #print("Username Already Exists")
    else:
        flag = False
        print("Username Does Not Exist")
    conn.close()
    return flag
#check_uname('laraib')
#check_uname('auguigi')




# --------------- SIGN_UP --------------- #
def sign_up(p1,p2):
    conn = db_conn()
    cursor = conn.cursor()
    sql = "insert into user (uname, upass) values (%s,%s)"
    val = (p1,p2)
    #print("h1")
    cursor.execute(sql,val)
    #print("h2")
    conn.commit()
    conn.close()
    return True
#sign_up("hafsa" , "abc123")



# --------------- CHANGE_PASSWORD --------------- #
def change_password(p1,p2):
    conn = db_conn()
    cursor = conn.cursor()
    sql = "update user set upass = '" + p2 + "' where uname ='" + p1 + "'"
    #print("h1")
    cursor.execute(sql)
    #print("h2")
    conn.commit()
    conn.close()
    return True
#change_password("laraib", "abc123")
#print("Done")



"""
cursor= db.cursor()
cursor.execute("select * from user")
result = cursor.fetchall()
for i in range(len(result)):
	print(result[i])
"""


