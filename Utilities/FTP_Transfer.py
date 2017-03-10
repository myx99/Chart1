from ftplib import FTP
import time

date = time.strftime("%Y%m%d")

def ftpconnect():
    ftp_server = "172.16.15.100"
    username = "taoma"
    password = "tao@123"
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_server, 21)
    ftp.login(username, password)
    return ftp

def downloadfile():
    # remotepath = "/gz/%s/" % date
    remotepath = "/gz/20170301/NAV20170301"
    ftp = ftpconnect()
    print(ftp.getwelcome())
    print(ftp.nlst())
    bufsize = 1024
    localpath = "D:\\temp\\test\\"
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

def uploadfile():
    remotepath = "/gz/20170307/"
    ftp = ftpconnect()
    bufsize = 1024
    localpath = "D:\\temp\\test\\list.txt"
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

# uploadfile()

downloadfile()