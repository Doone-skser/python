# @author:九世
# @time:2019/7/3
# @file:mian.py

from gevent import monkey;monkey.patch_all()
import gevent
import config.config
import requests
from multiprocessing import Process
from gevent.lock import RLock

ok=[]
lock=RLock()
black=['404','Not Found','找不到','黑名单','安全狗','拦截']

class scan(object):
    def __init__(self,url):
        self.url=url
        self.thread=[]
        self.rw=[]
        print('\033[1;32m[+]\033[0m 找到以下路径：')
        self.djc()

    def scan(self,path):
        lock.acquire()
        url=str(self.url).rstrip('/')+'/'+path
        try:
            rqt=requests.get(url=url,headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
            for blacks in black:
                if blacks not in rqt.text and rqt.status_code==200:
                    if rqt.url not in ok:
                        print(rqt.url)
                    else:
                        continue
                    ok.append(rqt.url)
        except:
            pass
        lock.release()

    def xc(self,path):
        for r in path:
            self.rw.append(gevent.spawn(self.scan,r))

        gevent.joinall(self.rw)

    def djc(self):
        calc=0
        path=config.config.DIRE_PATH
        dk=open(path,'r',encoding='utf-8')
        for q in dk.readlines():
            qc="".join(q.split('\n'))
            if calc==config.config.DIRECTORY:
                p=Process(target=self.xc,args=(self.thread,))
                p.start()
                calc=0
                self.thread.clear()
            self.thread.append(qc)
            calc+=1

        if len(self.thread)>0:
            p = Process(target=self.xc, args=(self.thread,))
            p.start()