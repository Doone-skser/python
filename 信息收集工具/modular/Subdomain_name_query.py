# @author:九世
# @time:2019/7/2
# @file:mian.py

from gevent import monkey;monkey.patch_all()
import requests
import config.config
import warnings
import gevent
from multiprocessing import Process
import dns.resolver
from bs4 import BeautifulSoup
from gevent.lock import RLock

warnings.simplefilter("ignore", category=UserWarning)

domains=[]
lock=RLock()

def domain_query():
    def wrater(func):
        def query(*args,**kwargs):
            print('\033[1;32m[+]\033[0m 域名查询:')
            headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
            url='http://site.ip138.com/{}/domain.htm'.format(*args)
            rqt=requests.get(url=url,headers=headers)
            rgt=BeautifulSoup(rqt.text,'html.parser').find_all('a',target='_blank')
            for c in rgt:
                if  str(*args) in str(c):
                    domains.append(c.get_text())
            return func(*args,**kwargs)
        return query
    return wrater

def domain_baopo():
    def wrter(func):
        def bp(*args,**kwargs):
            lock.acquire()
            path=r'dict/domain.txt'
            dp=[]
            dk=open(path,'r',encoding='utf-8')
            for d in dk.readlines():
                dp.append("{}.{}".format("".join(d.split('\n')),*args))
            lock.release()
            return func(dp,**kwargs)
        return bp
    return wrter

@domain_query()
def run(url):
    pass


def dns_b(domain):
    try:
        querys=dns.resolver.query(domain,'A')
        for q in querys:
            domains.append(domain)
    except:
        pass

def xc(rg):
    rt=[]
    try:
        for r in rg:
            rt.append(gevent.spawn(dns_b,r))
        gevent.joinall(rt)

    except:
        pass

@domain_baopo()
def run2(url):
    print('\033[1;32m[+]\033[0m 字典爆破域名开始')
    rw=[]
    calc=0
    for c in url:
        if calc==config.config.SUBDOMAIN:
            p=Process(target=xc,args=(rw,))
            p.start()
            calc=0
            rw.clear()
        rw.append(c)
        calc+=1

    if len(rw)>0:
        p = Process(target=xc, args=(rw,))
        p.start()

def cat():
    qc=list(set(domains))
    for q in qc:
        print(q)