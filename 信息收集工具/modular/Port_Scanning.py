# @author:九世
# @time:2019/7/2
# @file:mian.py

import gevent
from gevent import monkey
monkey.patch_all()
import config.config
from multiprocessing import Process
from gevent.lock import RLock
import socket

lock=RLock()

def portscan(host,port):
    global recvs
    lock.acquire()
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host,port))
        s.sendall(b'banner')
        recvs=s.recv(1024)
        print('\033[1;32m[+]\033[0m {}/Open banner:{}'.format(port,recvs.decode('utf-8')))
    except Exception as r:
        if "'utf-8' codec can't decode" in str(r):
            print('\033[1;32m[+]\033[0m {}/Open banner:{}'.format(port, recvs))
        pass
    lock.release()
def xc(url,rw):
    rg=[]
    for i in rw:
        rg.append(gevent.spawn(portscan,url,i))

    gevent.joinall(rg)


def run(url):
    rw=[]
    calc=0
    for i in range(1000):
        if calc==config.config.THREAD:
            p=Process(target=xc,args=(url,rw))
            p.start()
            calc=0
            rw.clear()
        rw.append(i)
        calc+=1

    if len(rw)>0:
        p = Process(target=xc, args=(url,rw))
        p.start()