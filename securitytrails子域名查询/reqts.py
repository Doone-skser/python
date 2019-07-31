#@:author:九世
#@:time:2019/7/31
#@:file:reqts.py

from gevent import monkey;monkey.patch_all()
from multiprocessing import Process
from gevent import lock
import gevent
import os
import requests
from bs4 import BeautifulSoup

Rlock=lock.RLock()
class Rgbtsqeury:
    def __init__(self):
        self.file='save.txt'
        self.calc=0
        self.djcs=[]
        self.xcs=[]
        self.headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    def reqts(self,url):
        if 'https://' in url:
            pass
        else:
            url='http://'+url
        try:
            rqt=requests.get(url=url,headers=self.headers)
            if rqt.status_code==200 and len(rqt.text)>0:
                title=str(BeautifulSoup(rqt.text,'html.parser').find('title')).replace('<title>','').replace('</title>','').replace('\n','').rstrip()
                ld=[x for x in rqt.headers]
                if 'Server' in ld:
                    server=rqt.headers['Server']
                else:
                    server=''

                if 'X-Powered-By' in ld:
                    xf=rqt.headers['X-Powered-By']
                else:
                    xf=''

                print('url:{} title:{} server:{} X-Powered-By:{}'.format(rqt.url,title,server,xf))
                print('url:{} title:{} server:{} X-Powered-By:{}'.format(rqt.url, title, server, xf),file=open('request.txt','a'))
        except Exception as error:
            if 'requests.exceptions.SSLError' in str(error):
                url='https://{}'.format(url)
                self.reqts(url)

    def xc(self,rw):
        Rlock.acquire()
        for r in rw:
            self.xcs.append(gevent.spawn(self.reqts, r))
        Rlock.release()

        gevent.joinall(self.xcs)

    def djc(self):
        if os.path.exists(self.file):
            print('[+] save.txt存在')
        else:
            print('[-] 请先查询子域名生成save.txt')
            exit()

        dk = open(self.file, 'r', encoding='utf-8')
        for r in dk.readlines():
            data = "".join(r.split('\n'))
            if self.calc == 10:
                p = Process(target=self.xc, args=(self.djcs,))
                p.start()
                self.calc = 0
                self.djcs.clear()
            self.djcs.append(data)
            self.calc += 1

        if len(self.djcs) > 0:
            p = Process(target=self.xc, args=(self.djcs,))
            p.start()