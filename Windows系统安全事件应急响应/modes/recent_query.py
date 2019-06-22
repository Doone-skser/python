#author:九世
#time:2019/6/22
#file:recent_query.py

import os

def hq():
    print('[+] 获取用户最近访问的文件路径')
    user=os.popen('echo %username%')
    username=user.read()
    rst=os.popen('dir C:\\Users\\{}\\Recent'.format(str(username).replace('\n','').strip().lstrip().rstrip()))
    print(rst.read())