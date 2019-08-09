import requests

proixy={'http':'http://127.0.0.1:4444','https':'https://127.0.0.1:4444'}
rqt=requests.post(url='https://www.baidu.com/sss',headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'},proxies=proixy)
print(rqt.text)