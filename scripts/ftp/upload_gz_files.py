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

#-#   Section: Download   #-#

# local -> ftp for Valuation files
def local_to_ftp_gz(tag=None):
    # connect to ftp
    ftp = __ftp_connection_init__()

    if tag == None:
        date = time.strftime("%Y%m%d")
    else:
        date = tag

    # set path
    remote_path = "/gz"
    ftp.cwd(remote_path)

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if not date in ftp_folder_list:
        ftp.mkd(date)
    ftp_file_path = remote_path + "/" + date
    ftp.cwd(ftp_file_path)

    # set local path
    local_path = "V:\\inner\\gz\\%s\\" % date

    # file list check
    product1 = "GZFB0001.dbf"
    product2 = "GZFB0002.dbf"
    NAV_file = "NAV" + "%s" % date
    file_list = [product1, product2, NAV_file]

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


# ---  Single day transfer  --- #

### daily upload gz files  ###
local_to_ftp_gz()
