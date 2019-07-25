'''
fofa抓取第二代
'''
from gevent import monkey;monkey.patch_all()
from multiprocessing import  Process
from gevent.lock import  RLock
import sys
import time
import requests
import gevent
import base64
import re
import optparse

lock=RLock()
xcs=[]
html=''
write,flush=sys.stdout.write,sys.stdout.flush


class FOFA:
    def __init__(self):
        self.cookies={}
        self.cookie='<COOKIE>' #cookie
        for c in self.cookie.split(';'):
            key,value=c.split('=',1)
            self.cookies[key]=value

        usage='search.py -s [搜索的关键字] -p [页数]'
        opt=optparse.OptionParser(usage)
        opt.add_option('-s',dest='search',help='搜索的关键字')
        opt.add_option('-p',dest='page',help='搜索的页数')
        (options,args)=opt.parse_args()
        if options.search and options.page:
            self.guanjianzi=options.search
            self.djc(page=options.page)
        else:
            opt.print_help()
            exit()

    def djc(self,page):
        print('[+] 请求fofa')
        print('[+] 提取url和title写入xls')
        djcs=[]
        calc=0
        for r in range(1,int(page)+1):
            if calc==10:
                p=Process(target=self.xc,args=(djcs,))
                p.start()
                calc=0
                djcs.clear()
            djcs.append(r)
            calc+=1
        if len(djcs)>0:
            p = Process(target=self.xc, args=(djcs,))
            p.start()

    def xc(self,rw):
        lock.acquire()
        for r in rw:
            urls='https://fofa.so/result?page={}&qbase64={}'.format(r,bytes.decode(base64.b64encode(bytes(self.guanjianzi,encoding='utf-8'))))
            xcs.append(gevent.spawn(self.search,urls,1))
        lock.release()

        gevent.joinall(xcs)
        self.fj()

    def search(self,url,id):
        if int(id)==0:
            time.sleep(10)
        try:
            rqt=requests.get(url=url,headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'},cookies=self.cookies)
            if 'Retry later' in rqt.text:
                print('[!] 跑太快被fofa给禁了，等待10秒重新请求')
                self.search(url,0)
            else:
                global html
                html+=rqt.text
        except:
            pass

    def fj(self):
        calc=0
        urls=re.findall('<a target="_blank" href=".*">.* <i class="fa fa-link"></i></a>',html)
        title=re.findall('<i  aria-hidden="true"></i>\n .*',html)
        for h in title:
            calc+=1
            title=str(h).replace('<i  aria-hidden="true"></i>','').replace('</li>','').replace(' ','').replace('\n','')
            print(title, file=open('save_title.txt', 'a', encoding='utf-8'))
            data = 'write:{}\n'.format(title)
            write(data)
            flush()
            time.sleep(.1)
            write('\x08' * len(data))

        calc=0
        for t in urls:
            calc+=1
            href=str(t).split('>')
            url=str(href[0]).replace('<a target="_blank" href="','').replace('"','')
            print(url,file=open('save_url.txt','a',encoding='utf-8'))
            data = 'write:{}\n'.format(url)
            write(data)
            flush()
            time.sleep(.1)
            write('\x08' * len(data))
        print('[+] 写入完成')

if __name__ == '__main__':
    obj=FOFA()