import urllib.request
import re

# replace 4 remote directory address

remote_dir = 'http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/'
url_path = urllib.request.urlopen(remote_dir)
real_path = url_path.read().decode('utf-8')

# replace 4 RegEx

file_pattern = re.compile("([\w\.-]+[\.]pdf)")
file_list = set(file_pattern.findall(real_path))
print(file_list)



for f in file_list:
    remote_file = urllib.request.urlopen(remote_dir + f)
    print('Copying file:', f, end='')
    local_file = open(f, 'wb')
    local_file.write(remote_file.read())
    local_file.close()
    print(' Done.')
    remote_file.close()
