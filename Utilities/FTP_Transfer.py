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
    ftp.encoding = 'gb2312'   # To fix the file names with Chinese characters
    return ftp

#------------#   Transfer Script   #-----------#

#-#   Section: Download   #-#


# local -> ftp for Valuation files
def local_to_ftp_gz(tag=None):
    # connect to ftp
    ftp = __ftp_connection_init__()

    if tag is None:
        date = time.strftime("%Y%m%d")
    else:
        date = tag

    # set path
    remote_path = "/gz"
    ftp.cwd(remote_path)

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if date not in ftp_folder_list:
        ftp.mkd(date)
    ftp_file_path = remote_path + "/" + date
    ftp.cwd(ftp_file_path)

    # set local path
    local_path = "V:\\inner\\gz\\%s\\" % date

    # file list check
    product1 = "GZFB0001.dbf"
    product2 = "GZFB0002.dbf"
    nav_file = "NAV" + "%s" % date
    file_list = [product1, product2, nav_file]

    # file transfer
    bufsize = 1024
    for parent, dirnames, filenames in os.walk(local_path):
        for file in filenames:
            if file in file_list:
                file_name = local_path + file
                fp = open(file_name, 'rb')
                ftp.storbinary("STOR " + file, fp, bufsize)
                fp.close()

    # close connect
    ftp.set_debuglevel(0)
    ftp.quit()


# local -> ftp for future settlement files   TODO: only for future trades, need enrich if trade A-shares
def local_to_ftp_ft(tag=None):
    # connect to ftp
    ftp = __ftp_connection_init__()

    if tag is None:
        date = time.strftime("%Y%m%d")
    else:
        date = tag

    # set path
    remote_path = "/gzouter"
    ftp.cwd(remote_path)

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if date not in ftp_folder_list:
        ftp.mkd(date)
    ftp_file_path = remote_path + "/" + date
    ftp.cwd(ftp_file_path)

    # set local path
    local_path = "V:\\gzouter\\%s\\" % date
    # local_path = "E:\\data\\gzouter\\%s\\" % date

    # file transfer
    bufsize = 1024
    for parent, dirnames, filenames in os.walk(local_path):
        for file in filenames:
            if file[-4:] == ".txt":   # future settlement files are type of TXT
                file_name = local_path + file
                fp = open(file_name, 'rb')
                ftp.storbinary("STOR " + file, fp, bufsize)
                fp.close()

    # close connect
    ftp.set_debuglevel(0)
    ftp.quit()


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
    nav_file = "NAV" + "%s" % date
    file_list = [product1, product2, nav_file]

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


# ftp -> local ft files
def ftp_to_local_ft(tag=None):
    # connect to ftp
    ftp = __ftp_connection_init__()

    if tag is None:
        date = time.strftime("%Y%m%d")
    else:
        date = tag

    # general settings
    remote_path = "/gzouter/%s" % date
    local_path_with_date = "E:\\data\\gzouter\\%s\\" % date

    # create folder for files to be downloaded
    if not os.path.exists(local_path_with_date):
        os.mkdir(local_path_with_date)

    # get ftp file list
    ftp.cwd(remote_path)
    ftp_file_list = ftp.nlst()

    # file transfer
    bufsize = 1024
    for f in ftp_file_list:
        if f[-4:] == ".txt":
            file_name = local_path_with_date + f
            fp = open(file_name, 'wb')
            ftp.retrbinary("RETR " + f, fp.write, bufsize)
            fp.close()

    # close connect
    ftp.set_debuglevel(0)
    ftp.quit()