# @author:九世
# @time:2019/7/2
# @file:mian.py

URL='https://xkb.com.au' #输入要进行探测的url
DOMAIN='xkb.com.au' #输入要进行探测的域名
THREAD=100 #协程设置
XIANC=20 #进程数设置
DIRECTORY=10000 #目录扫描的协程设置
SUBDOMAIN=10000 #子域名爆破协程设置
DOMAIN_BAOPO=0 #0为不开启子域名爆破，1为开启
DIRE_PATH=r'dict/scan.txt' #引用dict目录下的指定字典