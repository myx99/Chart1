import ftplib as fb

ftp = fb.FTP(host="172.16.15.100", user="taoma", passwd="tao@123")
print(ftp.nlst())
