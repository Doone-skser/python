# @author:九世
# @file:main.py
# @time:2019/7/8

from gevent import monkey;monkey.patch_all()
from gevent.lock import RLock
from multiprocessing import Process
from bs4 import BeautifulSoup
import re
import config.config
import gevent
import requests

lock=RLock()
domain={}

class Butian:
    def __init__(self):
        self.cookies={}
        self.company_id=[]
        self.look_id=config.config.LOOK_ID
        self.url=config.config.URL
        self.version=config.config.VERSION
        self.id=config.config.ID
        self.set_id=config.config.SET_ID
        self.cookie=config.config.COOKIE
        self.wait=config.config.WAIT
        self.page=config.config.PAGE
        self.process=config.config.PROCESS
        self.calc=0
        self.proces=[]
        self.request=requests.session()
        self.runid=[]
        for cook in str(self.cookie).split(';'):
            key,value=cook.split('=',1)
            self.cookies[key]=value

    def banner(self):
        banner='''
                                  ,--.--------.  .=-.-.  ,---.      .-._         
    _..---.  .--.-. .-.-./==/,  -   , -\/==/_ /.--.'  \    /==/ \  .-._  
  .' .'.-. \/==/ -|/=/  |\==\.-.  - ,-./==|, | \==\-/\ \   |==|, \/ /, / 
 /==/- '=' /|==| ,||=| -| `--`\==\- \  |==|  | /==/-|_\ |  |==|-  \|  |  
 |==|-,   ' |==|- | =/  |      \==\_ \ |==|- | \==\,   - \ |==| ,  | -|  
 |==|  .=. \|==|,  \/ - |      |==|- | |==| ,| /==/ -   ,| |==| -   _ |  
 /==/- '=' ,|==|-   ,   /      |==|, | |==|- |/==/-  /\ - \|==|  /\ , |  
|==|   -   //==/ , _  .'       /==/ -/ /==/. /\==\ _.\=\.-'/==/, | |- |  
`-._`.___,' `--`..---'         `--`--` `--`-`  `--`        `--`./  `--`  
        version:{}
        author:九世
        github:https://github.com/422926799
        '''.format(self.version)
        print(banner)

    def yzm_rz(self,rqt):
        if '网站当前访问量较大' in rqt.content.decode('utf-8'):
            print('[验证码] 验证码下载到yzm文件夹里,请手动输入验证码:{}'.format(rqt.url))
            text = BeautifulSoup(rqt.text, 'html.parser').find('img').get('src')
            yzm_url = self.url + text
            wt = open('yzm/yzm.jpg', 'wb')
            download = self.request.get(url=yzm_url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'},cookies=self.cookies)
            wt.write(download.content)
            wt.close()
            user = input('验证码>')
            jg = self.url + '/waf_verify.htm?captcha={}'.format(user)
            rqt = self.request.get(url=jg, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'},cookies=self.cookies)
            if not 'waf' in rqt.url:
                print('[+] 验证码已通过')

            return rqt

    def zhuaqu(self):
        urls=str(self.url)+str(self.id[self.set_id])
        for b in range(int(self.page)):
            rqt=self.request.post(url=urls,headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'},cookies=self.cookies,data={'s':'1','p':'{}'.format(b)})
            if 'waf' in rqt.url:
                rqt=self.yzm_rz(rqt)
            json=rqt.json()['data']['list']
            for id in json:
                self.company_id.append(id['company_id'])

    def caiji(self,urls):
        rbt=self.request.get(url=urls,headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'},cookies=self.cookies)
        if 'waf' in rbt.url:
            rbt = self.yzm_rz(rbt)
        data=re.findall('placeholder="请输入厂商域名" value=".*"',rbt.text)
        name=re.findall('placeholder="漏洞属于哪个厂商" value=".*"',rbt.text)
        data_s=str(data[0]).replace('placeholder="请输入厂商域名" value="','').replace('"','')
        names_s=str(name[0]).replace('placeholder="漏洞属于哪个厂商" value="','').replace('"','')
        domain[names_s]=data_s

    def write_file(self):
        key=list(domain.keys())
        value=list(domain.values())
        for u in range(0,len(key)):
            print("'厂商名称':'{}','url':'{}'".format(key[u],value[u]))
            print("'厂商名称':'{}','url':'{}'".format(key[u], value[u]),file=open('save.txt','a',encoding='utf-8'))

    def run(self,rw):
        lock.acquire()
        for r in rw:
            urls=str(self.look_id).format(r)
            self.runid.append(gevent.spawn(self.caiji,urls))
        lock.release()
        gevent.joinall(self.runid)
        self.write_file()

    def run_process(self):
        self.banner()
        self.zhuaqu()
        for i in self.company_id:
            if self.calc==self.process:
                p=Process(target=self.run,args=(self.proces,))
                p.start()
                self.proces.clear()
                self.calc=0
            self.proces.append(i)
            self.calc+=1
        if len(self.proces)>0:
            p = Process(target=self.run, args=(self.proces,))
            p.start()

if __name__ == '__main__':
    obj=Butian()
    obj.run_process()