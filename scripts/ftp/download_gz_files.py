from ftplib import FTP
import time
import os


# internal function for init FTP connection
def __ftp_connection_init__():
    ftp_server = "172.16.15.100"
    username = "taoma"
    password = "tao@123"
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_server, 21)
    ftp.login(username, password)
    return ftp

#------------#   Transfer Script   #-----------#

#-#   Section: Upload   #-#


# ftp -> local gz files
def ftp_to_local_gz(tag=None):
    # connect to ftp
    ftp = __ftp_connection_init__()

    if tag is None:
        date = time.strftime("%Y%m%d")
    else:
        date = tag

    # general settings
    remote_path = "/gz/%s" % date
    local_path_with_date = "E:\\data\\gz\\%s\\" % date

    # create folder for files to be downloaded
    if not os.path.exists(local_path_with_date):
        os.mkdir(local_path_with_date)

    # get ftp file list
    ftp.cwd(remote_path)
    ftp_file_list = ftp.nlst()

    # target file list
    product1 = "GZFB0001.dbf"
    product2 = "GZFB0002.dbf"
    product3 = "GZFB0003.dbf"
    product4 = "GZFB0004.dbf"
    nav_file = "NAV" + "%s" % date
    file_list = [product1, product2, product3, product4, nav_file]

    # file transfer
    bufsize = 1024
    for f in ftp_file_list:
        if f in file_list:
            file_name = local_path_with_date + f
            fp = open(file_name, 'wb')
            ftp.retrbinary("RETR " + f, fp.write, bufsize)
            fp.close()

    # close connect
    ftp.set_debuglevel(0)
    ftp.quit()


# Main
ftp_to_local_gz("20170705")

