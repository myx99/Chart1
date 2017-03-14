from ftplib import FTP
import time
import os


date = time.strftime("%Y%m%d")

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

# local -> ftp for Valuation files
def local_to_ftp_gz_files():
    # connect to ftp
    ftp = __ftp_connection_init__()

    # set path
    root_path = "/gz"
    daily_folder = date
    ftp.cwd(root_path)

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if not daily_folder in ftp_folder_list:
        ftp.mkd(daily_folder)
    ftp_file_path = root_path + "/" + daily_folder
    ftp.cwd(ftp_file_path)

    # set local path
    bufsize = 1024
    local_path = "V:\\inner\\gz\\%s\\" % date

    # file list check
    product1 = "GZFB0001.dbf"
    product2 = "GZFB0002.dbf"
    NAV_file = "NAV" + "%s" % date
    file_list = [product1, product2, NAV_file]
    for parent, dirnames, filenames in os.walk(local_path):
        for file in filenames:
            if file in file_list:
                file_name = local_path + file
                fp = open(file_name, 'rb')
                ftp.storbinary("STOR " + file, fp, bufsize)

    # close connect
    ftp.set_debuglevel(0)
    ftp.close()
    ftp.quit()

# local -> ftp for future settlement files   TODO: only for future trades, need enrich if trade A-shares
def local_to_ftp_settlement_files():
    # connect to ftp
    ftp = __ftp_connection_init__()

    # set path
    root_path = "/gzouter"
    daily_folder = date
    ftp.cwd(root_path)

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if not daily_folder in ftp_folder_list:
        ftp.mkd(daily_folder)
    ftp_file_path = root_path + "/" + daily_folder
    ftp.cwd(ftp_file_path)

    # set local path
    bufsize = 1024
    local_path = "V:\\gzouter\\%s\\" % date

    # file type check
    for parent, dirnames, filenames in os.walk(local_path):
        for file in filenames:
            if file[-4:] == ".txt":   # future settlement files are type of TXT
                file_name = local_path + file
                fp = open(file_name, 'rb')
                ftp.storbinary("STOR " + file, fp, bufsize)

    # close connect
    ftp.set_debuglevel(0)
    ftp.close()
    ftp.quit()

# abstract to 1 function for upload
def local_to_ftp(keyword):
    # connect to ftp
    ftp = __ftp_connection_init__()

    # use keyword to idenity the target objects
    if keyword == "gz":
        remote_path = "/gz"
        local_path = "V:\\inner\\gz\\%s\\" % date
    elif keyword == "ft":
        remote_path = "/gzouter"
        local_path = "V:\\gzouter\\%s\\" % date
    else:
        print("Invalid function call, need a keyword")
        return

    # general settings
    daily_folder = date
    ftp.cwd(remote_path)
    bufsize = 1024

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if not daily_folder in ftp_folder_list:
        ftp.mkd(daily_folder)
    ftp_file_path = remote_path + "/" + daily_folder
    ftp.cwd(ftp_file_path)

    if keyword == "gz":
        # file list check
        product1 = "GZFB0001.dbf"
        product2 = "GZFB0002.dbf"
        NAV_file = "NAV" + "%s" % date
        file_list = [product1, product2, NAV_file]
        # file transfer
        for parent, dirnames, filenames in os.walk(local_path):
            for file in filenames:
                if file in file_list:
                    file_name = local_path + file
                    fp = open(file_name, 'rb')
                    ftp.storbinary("STOR " + file, fp, bufsize)
    elif keyword == "ft":
        # file transfer
        for parent, dirnames, filenames in os.walk(local_path):
            for file in filenames:
                if file[-4:] == ".txt":  # future settlement files are type of TXT
                    file_name = local_path + file
                    fp = open(file_name, 'rb')
                    ftp.storbinary("STOR " + file, fp, bufsize)

    # close connect
    ftp.set_debuglevel(0)
    ftp.close()
    ftp.quit()

# for download
def ftp_to_local(keyword):
    # connect to ftp
    ftp = __ftp_connection_init__()

    # use keyword to idenity the target objects
    if keyword == "gz":
        remote_path = "/gz/%s" % date
        local_path = "E:\\data\\gz\\"
    elif keyword == "ft":
        remote_path = "/gzouter/%s" % date
        local_path = "E:\\data\\gzouter\\"
    else:
        print("Invalid function call, need a keyword")
        return

    # general settings
    daily_folder = date
    ftp.cwd(remote_path)
    bufsize = 1024

    # create folder for files to be uploaded
    ftp_folder_list = ftp.nlst()
    if not daily_folder in ftp_folder_list:
        ftp.mkd(daily_folder)
    ftp_file_path = remote_path + "/" + daily_folder
    ftp.cwd(ftp_file_path)

    if keyword == "gz":
        # file list check
        product1 = "GZFB0001.dbf"
        product2 = "GZFB0002.dbf"
        NAV_file = "NAV" + "%s" % date
        file_list = [product1, product2, NAV_file]
        # file transfer
        for parent, dirnames, filenames in os.walk(local_path):
            for file in filenames:
                if file in file_list:
                    file_name = local_path + file
                    fp = open(file_name, 'rb')
                    ftp.storbinary("STOR " + file, fp, bufsize)
    elif keyword == "ft":
        # file transfer
        for parent, dirnames, filenames in os.walk(local_path):
            for file in filenames:
                if file[-4:] == ".txt":  # future settlement files are type of TXT
                    file_name = local_path + file
                    fp = open(file_name, 'rb')
                    ftp.storbinary("STOR " + file, fp, bufsize)

    # close connect
    ftp.set_debuglevel(0)
    ftp.close()
    ftp.quit()









# def downloadfile():
#     # remotepath = "/gz/%s/" % date
#     remotepath = "/gz/20170301/NAV20170301"
#     ftp = ftpconnect()
#     print(ftp.getwelcome())
#     print(ftp.nlst())
#     bufsize = 1024
#     localpath = "D:\\temp\\test\\"
#     fp = open(localpath, 'wb')
#     ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
#     ftp.set_debuglevel(0)
#     fp.close()
#     ftp.quit()
