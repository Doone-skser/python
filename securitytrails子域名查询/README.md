## 暴躁的子域名信息收集工具 ##

query.py---抓取securitytrails的查询接口获取的子域名\
found.py---判断是否有CDN并获取IP区分有CDN和无CDN的域名\
reqts.py---获取存活的域名和域名的标题，Server头，X-Powered-By头信息\
main.py---调用上面三个的

```txt
保存为foundcdndomain.txt---存放的是有CDN的域名
保存为notfoundcdndomain.txt--存放的是没有CDN的域名，并获取到真实IP
保存为request.txt---存放的是存活的子域名和子域名标题信息，Server头信息，X-Powered-By头信息
```

PS:此工具之所以能成功由于，securitytrails.com的API接口，里的CSRF_TOKEN后端并没有效验
估计开发偷懒咯 ~-~