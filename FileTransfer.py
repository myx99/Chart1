import shutil as st
import time
import os


# source file
date = time.strftime("%Y%m%d")

s_path = "C:\\temp\\%s" % date
print(s_path)


# define destination path
d_path = "d:\\temp\\%s" % date
if not os.path.exists(d_path):
    os.mkdir(d_path)
    print(d_path + " is created!")

# copy file from path1 to path2
for parent, dirnames, filenames in os.walk(s_path):
    for f in filenames:
        s_file = s_path + "\\" + f
        st.copy(s_file, d_path)
        print(f + " has been copied!")

# for parent, dirnames, filenames in os.walk(d_path):
#     if file_name in filenames:
#         print(file + " has been copied!!")