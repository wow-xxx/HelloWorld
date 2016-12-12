import ftplib
import os
import linecache
from hashlib import md5
import config

confinit = config.configinit


serlist = os.path.join(os.getcwd(), 'serverlist')

def serverinfo():
    serinfos = linecache.getlines(serlist)
    serinfoline = (line[:-1] for line in serinfos)
    for serinfo in  serinfoline:
        a = serinfo.split(' ')
        yield a


def md5sum(logfile):
    m = md5()
    log_file = open(logfile, 'rb')
    m.update(log_file.read())
    log_file.close()
    logmd5 = m.hexdigest()
    return logmd5


def md5check((beforemd5,aftermd5)):
    if beforemd5 == aftermd5:
        return "ok"
    else:
        return "error"


ftpinfo = confinit.ftpinfo

def ftpdownload(ip,dir):
    target = '.'.join([ip,"log"])
    print ftpinfo['ftpport'], ftpinfo['timeout'], ftpinfo['ftpdir'], ftpinfo['ftpuser'], ftpinfo['ftppassword'],target
    try:
        f = ftplib.FTP(ip)
        f.connect(ip, ftpinfo['ftpport'], int(ftpinfo['timeout']))
    except:
        print 'ERROR:cannot reach " %s"' % ip
        ftpflag = '%s+%s download failed!' % (ip, target)
    try:
        f.login(ftpinfo['ftpuser'], ftpinfo['ftppassword'])
    except:
        print 'ERROR: cannot login anonymously'
        f.quit()
        ftpflag = '%s+%s download failed!' % (ip, target)
    try:
        f.cwd(ftpinfo['ftpdir'])
        bufsize = 1024
    except:
        print 'ERRORL cannot CD to "%s"' % ftpinfo['ftpdir']
        f.quit()
        ftpflag = '%s+%s download failed!' % (ip, target)
    try:
        os.chdir(dir)
        f.retrbinary('RETR %s' % target, open(target, 'wb').write, bufsize)
    except:
        print 'ERROR: cannot read file "%s"' % target
        os.remove(target)
        ftpflag = '%s+%s download failed!' % (ip, target)
    else:
        # os.system('iconv -f ISO-8859-1 -t utf8 %s' % logfile)
        print '*** Downloaded "%s %s" to CWD' % (ip, target)
        f.quit()
        return


def log():
    pass