#@:author:九世
#@:time:2019/7/31
#@:file:found.py

from gevent import monkey;monkey.patch_all()
from multiprocessing import Process
from gevent import lock
import warnings
import os
import re
import gevent

Rlock=lock.RLock()
warnings.filterwarnings("ignore")
class Found:
    def __init__(self):
        self.file='save.txt'
        self.calc=0
        self.djcs=[]
        self.xcs=[]

    def request(self,url):
        command='ping.exe -n 1 {}'.format(url)
        zx=os.popen(command)
        jg=zx.read()
        host = re.search('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',jg)
        founds=re.findall('正在 Ping .* [[]',jg)
        if len(founds)>0:
            domains=str(founds[0]).replace('正在 Ping ','').replace('[','').rstrip()
            if url==domains:
                print('不是CDN:{} IP:{}'.format(domains,host.group()))
                print('domain:{} IP:{}'.format(domains,host.group()),file=open('notfoundcdndoman.txt','a'))
            else:
                print('发现有CDN的域名,CDN:{} 域名:{}'.format(domains,url))
                print('cdn:{} domain:{}'.format(domains,url), file=open('foundcdndoman.txt', 'a'))


    def xc(self,rw):
        Rlock.acquire()
        for r in rw:
            self.xcs.append(gevent.spawn(self.request,r))
        Rlock.release()

        gevent.joinall(self.xcs)

    def djc(self):
        if os.path.exists(self.file):
            print('[+] save.txt存在')
        else:
            print('[-] 请先查询子域名生成save.txt')
            exit()

        dk=open(self.file,'r',encoding='utf-8')
        for r in dk.readlines():
            data="".join(r.split('\n'))
            if self.calc==10:
                p=Process(target=self.xc,args=(self.djcs,))
                p.start()
                self.calc=0
                self.djcs.clear()
            self.djcs.append(data)
            self.calc+=1

        if len(self.djcs)>0:
            p = Process(target=self.xc, args=(self.djcs,))
            p.start()