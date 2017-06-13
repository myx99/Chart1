import pymysql
import Common.GlobalConfig as gc


class MySQLConnection(object):

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'Matao_2012'
        self.db = 'test'
        self.use_unicode = True
        self.charset = "utf8"
        print("Initiation of MySQLConnection class is finished")

    def get_conn(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, use_unicode=self.use_unicode, charset=self.charset)
        print("Connected to MySQL DB")
        return self.conn

    def close_conn(self):
        self.conn.close()
        print("Closed connection with MySQL DB")

    def set_conn(self, connlist):
        connlist =
        self.host = gc.coonlist
        self.port = 3306
        self.user = 'root'
        self.passwd = 'Matao_2012'
        self.db = 'test'
        self.use_unicode = True
        self.charset = "utf8"


if __name__ == '__main__':
    m = MySQLConnection()
    m.get_conn()
    m.close_conn()
