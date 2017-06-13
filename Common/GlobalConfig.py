import ConfigParser



class GlobalConfig:
    def conn_list(self, matao_pc):
        host = '127.0.0.1'
        port = 3306
        user = 'root'
        passwd = 'Matao_2012'
        db = 'test'
        use_unicode = True
        charset = "utf8"
        return [host, port, user, passwd, db, use_unicode, charset]

if __name__ == '__main__':
    m = GlobalConfig()
    m.conn_list(matao_pc)





