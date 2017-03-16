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
    ftp.encoding = 'gb2312'
    return ftp

#------------#   Transfer Script   #-----------#

#-#   Section: Download   #-#

# local -> ftp for future settlement files   TODO: only for future trades, need enrich if trade A-shares
def local_to_ftp_ft(tag=None):
    # connect to ftp
    ftp = __ftp_connection_init__()

    if tag == None:
        date = time.strftime("%Y%m%d")
    else:
        date = tag

    # set path
    remote_path = "/gzouter"
    ftp.cwd(remote_path)

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if not date in ftp_folder_list:
        ftp.mkd(date)
    ftp_file_path = remote_path + "/" + date
    ftp.cwd(ftp_file_path)

    # set local path
    local_path = "V:\\gzouter\\%s\\" % date

    # file type check
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


# ---  Single day transfer  --- #

### daily upload ft files  ###
local_to_ftp_ft()