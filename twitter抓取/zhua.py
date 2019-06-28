#@author:九世
#@time:2019/6/28
#@file:zhua.py

import requests
import re
import conf.config
import gevent
import os
from multiprocessing import  Process
from bs4 import BeautifulSoup

tw_name=[]
tw_id=[]

class Zhua():
    def reads(self):
        if os.path.exists(conf.config.user_path):
            dk=open(conf.config.user_path,'r',encoding='utf-8')
            for d in dk.readlines():
                qc="".join(d.split('\n'))
                tw_name.append(qc)
        else:
            print('[-] 找不到文件')
            exit()

        print('[+] 要爬的用户名')
        print(tw_name)

    def reqt(self,username):
        global proxies,headers,cookies
        proxies=conf.config.proxies
        headers={
        'accept':'application/json, text/javascript, */*; q=0.01',
        'accept-encoding':'gzip, deflate, sdch, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'referer':'https://twitter.com/{}'.format(username),
        'x-requested-with':'XMLHttpRequest',
        'x-twitter-active-user':'yes'
        }
        cookies={}
        cookie=conf.config.cookie
        for c in cookie.split(';'):
            key,value=c.split('=',1)
            cookies[key]=value
        url='https://twitter.com/i/profiles/show/{}/media_timeline?for_photo_rail=true'.format(username)
        rqt=requests.get(url=url,headers=headers,proxies=proxies,cookies=cookies)
        js=rqt.json()['items_html']
        data_status_id=re.findall('data-status-id=.*',str(js))
        for s in data_status_id:
            tw_id.append(str(s).replace('data-status-id=','').replace('"',''))

    def djc(self):
        rw=[]
        calc=0
        for l in tw_id:
            if len(rw)==100:
                p=Process(target=self.xc,args=(rw,cookies,headers))
                p.start()
                calc=0
                rw.clear()
            rw.append(l)
            calc+=1

        if len(rw)>0:
            p = Process(target=self.xc, args=(rw,cookies,headers))
            p.start()

    def xc(self,rc,cookies,headers):
        rw=[]
        for r in rc:
            rw.append(gevent.spawn(self.getrespone,r,cookies,headers))

        print('[+] 抓取的内容')
        gevent.joinall(rw)

    def getrespone(self,id,cookies,headers):
        url='https://twitter.com/KitPloit/status/{}?conversation_id={}'.format(id,id)
        rqts=requests.get(url=url,headers=headers,proxies=conf.config.proxies,cookies=cookies)
        bt=BeautifulSoup(rqts.text,'html.parser')
        nam=re.findall('[/].*[/]status',str(rqts.url))
        name=str(nam[0]).replace('//twitter.com/','').replace('/status','')
        times=bt.find_all('span',class_="metadata")[0].get_text()
        if conf.config.times!='':
            if conf.config.times in times:
                print('用户名:{} 推特url:{} 时间:{}'.format(name,rqts.url,times))
                print('用户名:{} 推特url:{} 时间:{}'.format(name, rqts.url, times),file=open('save.txt','a',encoding='utf-8'))
                print('内容:')
                for b in bt.find_all('p',class_="TweetTextSize"):
                    print(b.get_text())
                    print(b.get_text(),file=open('save.txt','a',encoding='utf-8'))
                    print('')
        else:
            print('用户名:{} 推特url:{} 时间:{}'.format(name, rqts.url, times))
            print('用户名:{} 推特url:{} 时间:{}'.format(name, rqts.url, times), file=open('save.txt', 'a', encoding='utf-8'))
            print('内容:')
            for b in bt.find_all('p', class_="TweetTextSize"):
                print(b.get_text())
                print(b.get_text(), file=open('save.txt', 'a', encoding='utf-8'))
                print('')
if __name__ == '__main__':
    obj=Zhua()
    obj.reads()
    for k in tw_name:
        obj.reqt(k)

    obj.djc()