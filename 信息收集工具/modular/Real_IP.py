# @author:九世
# @time:2019/7/2
# @file:mian.py

import socket
import requests
import re
import IPy
from bs4 import BeautifulSoup

hosts=[]
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
def readl():
    def wrts(func):
        def ret(*args,**kwargs):
            s=socket.gethostbyname_ex(*args)
            zz=re.finditer('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',str(s))
            id=[]
            for c in zz:
                id.append(c)
            if len(id)>1:
                print('\033[1;33m[!]\033[0m 发现CDN')
            else:
                ips=re.findall("match='.*'",str(id[0]))
                ip=str(ips[0]).replace("'",'').replace('match=','')
                print('\033[1;32m[+]\033[0m 真实IP:{}'.format(ip))
                hosts.append(ip)

            return func(*args,**kwargs)
        return ret
    return wrts

def ip_query():
    def wty(func):
        def query(*args,**kwargs):
            url='http://www.ip138.com/ips138.asp?ip={}&action=2'.format(*args)
            rqt=requests.get(url=url,headers=headers)
            text=BeautifulSoup(rqt.content.decode('gbk'),'html.parser')
            print('\033[1;32m[+]\033[0mIP详细信息:{}'.format(str(text.find_all('ul')[0]).replace('<ul class="ul1"><li>','').replace('</li></ul>','')).replace('<li>','').replace('</li>','').replace('本站数据：',''))
            return func(*args,**kwargs)
        return query
    return wty

def panzhan_query():
    def js(func):
        def kuang(*args,**kwargs):
            rqt=requests.get(url='http://s.tool.chinaz.com/same?s={}&page='.format(*args),headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
            text=BeautifulSoup(rqt.text).find_all('a')
            if len(text)>0:
                for c in text:
                    zz=re.findall('onclick=".*" target="_blank"',str(c))
                    if len(zz)>0:
                        print(str(zz[0]).replace('onclick="window.open(','').replace("'",'').replace(')"','').replace(' ','').replace('target="_blank"',''))
                else:
                    print('没有查询到旁站信息')
            return func(*args,**kwargs)
        return kuang
    return js


def C_cha():
    def wtaer(func):
        def gts(*args,**kwargs):
            ip=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',str(*args))
            ips=str(ip[0]).replace(ip[0][-1],'0')
            ip=str(ips).replace('(','').replace(')','').replace("'",'').replace(',','.').strip().lstrip().replace(' ','')
            ipt=IPy.IP('{}/24'.format(ip))
            for x in ipt:
                rqt=requests.post(url='http://api.webscan.cc/',headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36','Accept': 'application/json, text/javascript, */*; q=0.01','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'http://www.webscan.cc','Referer': 'http://www.webscan.cc/'},data={'action': 'query','ip':x})
                if 'null' not in rqt.text:
                    print('IP:{}----站点:{}'.format(x,str(rqt.text).replace('[','').replace('{','').replace('}','').replace('\\','')).replace(']',''))
            return func(*args,**kwargs)
        return gts
    return wtaer

@ip_query()
def run2(host):
    pass

@panzhan_query()
def pan_query(hosts):
    pass

@C_cha()
def cduan(hosts):
    pass

@readl()
def run(url):
    if len(hosts)>0:
        run2(hosts[0])
        print('\033[1;32m[+]\033[0m 旁站查询')
        pan_query(hosts[0])
        print('\033[1;32m[+]\033[0m C段查询')
        cduan(hosts[0])
    else:
        print('\033[1;31m[-]\033[0m 由于有CDN，不进行IP查询、旁站查询、C段查询')

