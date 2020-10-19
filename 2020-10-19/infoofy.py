#!/usr/bin/env python3


from __future__ import print_function
import os
import stat
import sys
import time
import date


print("__________________________________________________________________________")
result = pyfiglet.figlet_format(" FILE INFORMATION VIEWER V 0.1")
print(result)

os.system("date")






if sys.version_info >= (3, 0):
    raw_input = input

file_name = raw_input("YOUR FILE: ")
count = 0
t_char = 0





try:
    with open(file_name) as f:

# Source: https://stackoverflow.com/a/1019572

        count = (sum(1 for line in f))
        f.seek(0)
        t_char = (sum([len(line) for line in f]))
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

except IOError:
    pass
except IsADirectoryError:
    pass

file_stats = os.stat(file_name)



file_info = {
    'fname': file_name,
    'fsize': file_stats[stat.ST_SIZE],
    'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_MTIME])),
    'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_ATIME])),
    'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_CTIME])),
    'no_of_lines': count,
    't_char': t_char
}




file_info_keys = ('file name', 'file size', 'last modified', 'last accessed',
                  'creation time', 'Total number of lines are',
                  'Total number of characters are')
file_info_vales = (file_info['fname'], str(file_info['fsize']) + " bytes",
                   file_info['f_lm'], file_info['f_la'], file_info['f_ct'],
                   file_info['no_of_lines'], file_info['t_char'])

for f_key, f_value in zip(file_info_keys, file_info_vales):
    print(f_key, ' =', f_value)

if stat.S_ISDIR(file_stats[stat.ST_MODE]):
    print("ITS A /DIR")
else:
    file_stats_fmt = ''
    print("\nNOT A /DIR")
    stats_keys = ("st_mode (protection bits)", "st_ino (inode number)",
                  "st_dev (device)", "st_nlink (number of hard links)",
                  "st_uid (user ID of owner)", "st_gid (group ID of owner)",
                  "st_size (file size bytes)",
                  "st_atime (last access time seconds since epoch)",
                  "st_mtime (last modification time)",
                  "st_ctime (time of creation Windows)")
    for s_key, s_value in zip(stats_keys, file_stats):
        print(s_key, ' =', s_value)
