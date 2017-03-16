from Utilities.FTP_Transfer import *
import os


# ---  Multiple days upload transfer  --- #


### batch download gz files   ###


### batch upload for gz files  ###
#  path = "V:\\inner\\gz\\"

### batch upload for ft files  ###
# path = "V:\\gzouter\\"
# # path = "E:\\data\\gzouter\\"
#
# days = []
# for parent, dirnames, filenames in os.walk(path):
#     for d in dirnames:
#         days.append(d)

# print(days)

# for day in days:
#     local_to_ftp_gz(day)
#     local_to_ftp_ft(day)


# ---  Single day transfer  --- #

### batch upload for gz files  ###
# local_to_ftp_gz("20170309")

### batch upload for ft files  ###
# local_to_ftp_ft("20170310")