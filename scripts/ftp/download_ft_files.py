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

#-#   Section: Upload   #-#


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


# Main
ftp_to_local_ft("20170704")

