#author:九世
#time:2019/6/22
#file:service_query.py

import os
import conf.config

#获取网络信息
def portopen():
    if conf.config.port!='':
        cmd='netstat -ant | findstr {}'.format(conf.config.port)
    else:
        cmd='netstat -ant'
    zx=os.popen(cmd)
    print('[+] 网络连接信息')
    print(zx.read())

    print('[+] 路由表')
    zx=os.popen('netstat -r')
    print(zx.read())


#防火墙信息
def netshs():
    print('[+] 防火墙配置信息')
    cmd='netsh firewall show all'
    jx=os.popen(cmd)
    print('[+] 防火墙配置')
    print(jx.read())

#进程检查
def jinc():
    print('[+] 进程信息查询')
    if conf.config.port != '':
        cmd='netstat -abno | find "{}"'.format(conf.config.port)
    else:
        cmd = 'netstat -abno'

    zx=os.popen(cmd)
    print(zx.read())

    if conf.config.pid != '':
        cmd='tasklist /svc | find "{}"'.format(conf.config.pid)
    else:
        cmd = 'tasklist /svc'

    zx=os.popen(cmd)
    print(zx.read())