
import MySQLdb
import config

confinit = config.configinit
mysqlinfo=confinit.mysqlinfo


def mysqlconnect():
    conn = MySQLdb.connect(host=mysqlinfo["mysqlip"],
                          user=mysqlinfo["mysqluser"],
                          passwd=mysqlinfo["mysqlpasswd"],
                          db=mysqlinfo["mysqldb"],
                          charset="utf8")
    cursor = conn.cursor()
    return cursor

def indatabases(cursor,sql):
    results = cursor.execute(sql)
    return results


def mysqlselect(sql):
    conn = MySQLdb.connect(host=mysqlinfo["mysqlip"],
                          user=mysqlinfo["mysqluser"],
                          passwd=mysqlinfo["mysqlpasswd"],
                          db=mysqlinfo["mysqldb"],
                          charset="utf8")
    cursor = conn.cursor()
#    sql = "select alias,name from users where userid=1;"
    results = cursor.execute(sql)
    return results
#    results = cursor.fetchall()
#    return results[0]

#    for result in results:
#       beformd5 = result[0]
#       aftermd5 = result[1]
def mysqlupdate():
    pass

def mysqlinsert():
    pass


def selectsql(ip):
    sql = "select alias,name from users where userid=1;"
#    sql = "select * from secinfo where ip=%s limit 1;" % (ip)
    return sql

def insertsql():
    sql = "insert "
    return sql

def updatesql():
    sql = "update"
    return sql