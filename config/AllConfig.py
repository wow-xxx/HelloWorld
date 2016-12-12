import os
import ConfigParser


class config_init:

    def __init__(self):
        self.config_path = os.path.join(os.getcwd(), 'secconfig.ini')
        if not os.path.isfile(self.config_path):
            print  "no secconfig.ini"
            exit
        else:
            pass

        self.conf = ConfigParser.ConfigParser()
        self.conf.read(self.config_path)

        self.logpath = os.path.join(self.conf.get('pylog','logpath'), self.conf.get('pylog','logname'))
        self.ftpinfo = {'timeout':self.conf.get('ftpinfo','ftptimeout'),
                        'ftpport':self.conf.get('ftpinfo','ftpport'),
                        'ftpdir':self.conf.get('ftpinfo','ftpdir'),
                        'ftpport':self.conf.get('ftpinfo','ftpport'),
                        'ftpuser':self.conf.get('ftpinfo','user'),
                        'ftppassword':self.conf.get('ftpinfo','password')}

        self.mysqlinfo = {'mysqlip':self.conf.get('mysql','mysqlserverip'),
                          'mysqluser':self.conf.get('mysql','user'),
                          'mysqlpasswd':self.conf.get('mysql','password'),
                          'mysqlport':self.conf.get('mysql','port'),
                          'mysqldb':self.conf.get('mysql','database'),
                          'mysqlsctb':self.conf.get('mysql','logtable')}

    def firstrun(self):
        self.servergroup = self.conf.options('server')
        for servertype in self.servergroup:
            if not os.path.exists(self.conf.get('logdowndir','{ser}logdir'.format(ser=servertype))):
                os.makedirs(self.conf.get('logdowndir','{ser}logdir'.format(ser=servertype)))
            if not os.path.exists(self.conf.get('standard','{ser}standarddir'.format(ser=servertype))):
                os.makedirs(self.conf.get('standard','{ser}standarddir'.format(ser=servertype)))

    def servergroup(self,gametype):
        self.servergroup = self.conf.options('server')
        for servertype in self.servergroup:
            gametypes = self.conf.get('server', servertype).split(',')
            if gametype in gametypes:
                return servertype

    def logdir(self,gametype):
        self.servergroup = self.conf.options('server')
        for servertype in self.servergroup:
            gametypes = self.conf.get('server', servertype).split(',')
            if gametype in gametypes:
                return self.conf.get('logdowndir','{ser}logdir'.format(ser=servertype))
            else:
                return "There is no corresponding type"

    def standdir(self,gametype):
        self.servergroup = self.conf.options('server')
        for servertype in self.servergroup:
            gametypes = self.conf.get('server', servertype).split(',')
            if gametype in gametypes:
                return self.conf.get('standard','{ser}standarddir'.format(ser=servertype))
            else:
                return "There is no corresponding type"

    def customdir(self):
        pass

