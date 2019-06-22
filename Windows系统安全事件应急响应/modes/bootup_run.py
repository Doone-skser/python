#author:九世
#time:2019/6/22
#file:bootup_run.py

import os
import conf.config

#列出一些开机自启动的注册表值
def boot_runquery():
    for c in conf.config.path:
        print('[+] 检测路径:{}'.format(c))
        zx=os.popen('REG.exe QUERY {}'.format(c))
        print(zx.read())
        print('')

    path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Startup'
    print('[+] 开机自启文件夹:{}'.format(path))
    hq=os.listdir(path)
    if len(hq)>0:
        for h in hq:
            print(h)
    else:
        print('[+]开机自启文件夹下没有文件')