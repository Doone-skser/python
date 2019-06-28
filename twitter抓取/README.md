### twitter抓取 ###
- [x] 获取指定用户名发的推文
- [x] 保存到txt
- [x] 支持时间过滤
- [x] 支持用户配置


### config.py说明 ###
```python
user_path='conf/user.txt' #存放着要抓的用户名的txt
proxy = '127.0.0.1:1080' #代理设置
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
cookie='' #你的cookie
times='' #时间过滤，如果不想设置请留空,times=''
```

user.txt示例：
```python
demonsec666
AmarSaar
WBGlIl
KitPloit
evilcos
HackwithGithub
```

### 截图 ###
程序运行图：
![](https://s2.ax1x.com/2019/06/29/ZQE8P0.png)

save.txt图：
![](https://s2.ax1x.com/2019/06/29/ZQEYxU.md.png)