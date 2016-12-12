#!/usr/bin/python
#encoding=utf-8
import config
from master import all
from  master import mysql
import time

__metaclass__ = type

'''
安检主模块：
1.配置文件加载初始化模块
2.下载游服日志模块
3.初始化安检信息模块
4.安检对比模块

'''


aa = time.time()

#加载配置文件
allconfig = config.configinit
#allconfig.firstrun()
#第一次运行时新建目录
#日志下载路径
a = allconfig.logdir('Cnmy')
#模板存放路径
b = allconfig.standdir('Cnmy')
#本脚本日志路径
c = allconfig.logpath

#all.serverinfo是每行服务器信息的列表

"""
def zero(ip):
    result = mysql.mysqlselect(mysql.selectsql(ip))
    print result
    if result == 0:
        mysql.mysqlinsert(mysql.insertsql())
    else:
        mysql.mysqlupdate(mysql.updatesql())

def firststep():
    pass


for i in all.serverinfo():
    print i[2],a
    all.ftpdownload(i[2],a)
    a = all.md5sum('/tmp/security/log/yf/192.168.122.11.log')
    print a
    zero(i[2])
"""
sql = "select alias,name from users where userid=1;"
cursor = mysql.mysqlconnect()
a = mysql.indatabases(cursor,sql)




"""



def zero('ip'):
    mysql.mysqlselect()
    if 数据库里有:
        mysql.update()更新对应的游服名等信息以防移服
    else:
        mysql.insert()对于新服进行添加

def firststep('服务器类型','项目','ip'):
    all.ftpdownload(ip,dir,target)
    all.md5sum(log)
    mysql.mysqlselect()查出新旧md5值
    旧md5,新md5 = 上一次md5,刚算的md5
    mysql.mysqlinsert()写入md5值

def secondstep('ip'):
    md5result = all.md5check()
    if md5result == "error":
        mysql.mysqlupdate()写入md5一致错误
    else:
        对比()
        mysql.update()写入对比结果

"""


print a
print b
print c
bb = time.time()

cc = bb - aa
print cc

'''
这是分隔
'''




#if __name__ == '__main__':


