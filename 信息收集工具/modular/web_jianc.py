# @author:九世
# @time:2019/7/2
# @file:mian.py

import requests

def web_server_shibie(url):
    rqt=requests.get(url=url,headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
    headers=rqt.headers
    try:
        if 'Server' or 'X-Powered-By' in headers:
            print('\033[1;32m[+]\033[0m web程序中间件信息')
            print(headers['Server'])
            print(headers['X-Powered-By'])
    except:
        pass

def error_jiance(url):
    print('\033[1;32m[+]\033[0m 站点404错误信息')
    rqt = requests.get(url=str(url).rstrip('/')+'/404', headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
    print(rqt.text.strip('\n'))