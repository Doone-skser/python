#author:九世
#time:2019/6/22
#file:schtasks_query.py

import os
import conf.config

def jiancha():
    print('[+] 寻找计划任务文件夹下的文件')
    for j in conf.config.tasks_path:
        hq=os.listdir(j)
        if len(hq)!=0:
            print('[+] 文件路径:{}'.format(j))
            for c in hq:
                print(c)
        else:
            print('[+] 文件路径:{}'.format(j))