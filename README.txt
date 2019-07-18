Hacker information collection, used to collect information about the target.
Direct operation of specific usage.
Example:
python3 Hacker Tool set.py
python3 Hacker information collection.py
python3 translate.py
python3 arp.py
Please modify the SMTP. Login and SMTP. Sendmail () parameters before calling the mailbox forge script.
Ddos.py is the user I wrote with python2.7 please
Self modify the attack target inside
Defense ddos
Defense ddos: please first execute install. Py =>fyddos.

Then the defense ddos script starts. If you are attacked by ddos, execute.

Netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq-c | sort -n.

Command to view your IP. Detailed article: http://www.cnblogs.com/haq5201314/p/8351960.html

python shell.py -h
-a  asp Trojan horse 
-j  jsap Trojan horse 
-p php Trojan horse 
-v Edition

python3 Sqllinject.py

python3 WebmasterTools.py
Usage: [-z Subdomain mining][-p Side of the station inquiries][-x http status query]

Options:
  -h, --help    show this help message and exit
  -z SUBDOMAIN  Subdomain mining
  -p SIDE       Side of the station inquiries
  -x HTTP       http status query

I didn't have time to go to school before I uploaded the scripts I finished.

My blog: http://www.cnblogs.com/haq5201314/




Distinguish.py用于批量安装工具包，方便大家安装工具


These scripts and methods of use are all in my blog. Please dig or use this script.

The updated scripts are as follows:
cms.py #For mining target CMS targets His accessories are data.json
csrfjiance.py #Used to detect CSRF vulnerabilities
sqlzhuruapi.py #This is a script for mass mining site SQL injection
urltiaozhuan.py #This is a script for mining URL jump holes
Distinguish.py #This is the two generation of an information collection script
dianjijieci.py #This is a script that excavated clicking hijacking



python3 exploitsearch.py
Usage: exploitsearch.py [options]

Options:
  -h, --help  show this help message and exit
  -m          Save the home directory in the local area
  -w          Save all the attack loads of Web
  -s SEARCH   search exploit
  -y          Save the Long-range all exploit
  -b          Save the local all exploit


CVE-2018-2894任意文件上传漏洞检测POC：在Weblogic任意上传文件里面


2018年7月31号新增加的
dedecms远程文件写入exp 15年的
phpcms中转注入漏洞批量验证

Linux信息收集脚本
直接在目标机运行就行，信息保存在save.txt

收集的信息有：
首先要获取系统信息：
系统名称
本地ip
主机名
本地dns
环境变量
shell程序
hosts文件
路由信息
arp缓存
计划任务
挂载磁盘
mail目录
history文件
home/root/bin/sbin目录

获取用户信息
当前权限
用户信息
本地用户
在线用户
hash加密规则
hash信息
用户组信息
最后登录信息
最后登录用户信息
所有用户的计划任务

安全扫描
是否能无密码sudo
conf配置文件
ssh的密钥文件
是否能root登录
敏感配置文件扫描
关键字含有config、web.xml、database、pass的文件
uid为0用户
敏感服务匿名
空密码用户
zip/tar.gz/sh/pl/py/rb/txt/bak后缀文件

cms_debug是一个集合多种CMS插件的项目 目前版本1.0，已集合Asp_CMS的插件
Cms_debug is a collection of multiple CMS plug-ins. Now version 1, the plugin that has already assembled Asp_CMS.


WDCP爆破是专门针对wdcp后台进行爆破的

云悉指纹用于识别web指纹

MS17010是自己闲着无聊写的检测脚本

ECShop-exploit ECSHOP RCE 漏洞复现教程：VULNSPY实验-ECShop <= 2.7.x 全系列版本远程代码执行高危漏洞利用

SPLOITUS抓取了一个不错的exploits搜索引擎

xss_payload
是用于进行xss检测的

LEFI
是用于进行文件包含漏洞扫描的

这段时间比较忙没有及时更新写的脚本，在此说声抱歉。很多写过的脚本，具体作用我也忘的差不多了
请各位自行使用和了解,Thanks

By 九世 time 2018.11.16 0:11

base64 _injection.py 是用于进行base64注入的脚本，他要求你先填写你的url，在填写里面的id
例如：http://xxx.com/ss.php?id=MTM
先填：http://xxx.com/ss.php?id=
在填ID=13
此脚本针对无防御的站点

测试站点：http://yyyhhg.com

搜索更多类似的站点:google语法：inurl:.php?id=MTM

Base64_injection.py is a script for base64 injection. It asks you to fill in your URL first and fill in the ID in it.
For example: http://xxx.com/ss.php?Id=MTM
First fill in: http://xxx.com/ss.php?Id=
Filling in ID=13
This script is for defenseless sites
Test site: http://yyyhhg.com
Search for more similar sites: Google grammar: inurl:. php? Id = MTM

By 九世 time:2018/12/2

c2项目是我第一个接触c2通信所写出来的脚本
具体使用方法：
server:demo.py IP port or demo.exe IP port
client:修改gc.html里的连接配置http://127.0.0.1/gc.html，连接服务器并执行命令（可过360）
视频:[c2通信实现—其他—视频高清在线观看-优酷](https://v.youku.com/v_show/id_XMzk2NDI2MjI0MA==.html?spm=a2hzp.8253869.0.0)


C2 project is my first script to contact C2 communication
Specific methods of use:
Server: demo.py IP port or demo.exe IP port
Client: Modify the connection configuration in gc.html http://127.0.0.1/gc.html, connect to the server and execute commands (up to 360)

BY 九世 2018/12/14

新c2是我重新写的一个，他支持端口扫描，交互式的shell，文件上传，Linux后渗透信息收集。不足：有一定的BUG，但是服务端不会断开连接。

The new c2, which I rewrote, supports port scanning, interactive shell, file upload, and post-Linux infiltration for information collection. Insufficiency: There are some BUGs, but the server will not disconnect.

By 九世 2018/12/30

更新了一个wifi_dos攻击脚本
功能有：
一键开启网卡监听模式
MAC洪水攻击
Deauch攻击
SSID扫描

Update a wifi_dos attack script
The functions are:
One-click Open Network Card Monitoring Mode
MAC flood attack
Deauch attack
SSID scan

祝各位新的一年新年快乐
Happy New Year to you all

By 九世 2019/1/4

2019/1/11添加了新的thinkphp_5.* 远程代码执行利用脚本
支持单个利用，与批量

New thinkphp_5. * Remote Code Execution Utilization Script was added to 2019/1/11
Support single use, batch

By 九世 2019/1/11

更新了之前写的网易云音乐搜索，其实这个就是抓网易云对应的音乐ID，然后去指定的地方下载
补天爬虫，为了方便各位挖洞者收集URL，做了个对应的爬虫。具体看里面的使用说明，可爬公益SRC和专属SRC子域名批量查询和单个查询

Update the previous written music search of Netease Cloud, in fact, this is the corresponding music ID of Netease Cloud, and then go to the designated place to download.
Butian crawler, in order to facilitate the excavators to collect URLs, made a corresponding crawler. See the instructions in detail, you can climb public SRC and exclusive SRC subdomain name batch query and single query.

By 九世 2019/1/19

UAC旁路是为了以后后渗透好做事所写
参考文章来源于：http://www.ggsec.cn

UAC Bypass is written to infiltrate good work in the future.
Reference article from: http://www.ggsec.cn
By 九世 2019/1/24

windows文件查询用于查询页面指定的路径，用于后渗透方便探索目标windows有没有敏感路径或者日志等等。由于方便携带我将其用url来解析获取路径在进行查询。windows-file.txt就是，扔到web容器下用windows-file.py输入url路径即可

Windows file query is used to query the path specified by the page, and it can be used to penetrate into the target windows to find out whether there are sensitive paths or logs, etc. Because it is easy to carry, I use URL to parse the access path and query it. Windows-file.txt is to throw it under the web container and enter the URL path with windows-file.py.

By 九世 2019/1/25

这是我研究了chm钓鱼所写出的，为了方便快速生成。将在file文件里面生成的start.html放入Easy CHM中生成对应的chm，将fanvicon.ico,放入
你的apache目录，Linux的话他会自动帮你移动，windows下的话不会。
chm钓鱼：https://422926799.github.io/2019/01/27/Chm-fishing/

By 九世 2019/1/27


This is what I wrote about chm fishing, in order to facilitate the rapid generation. Put the start.html generated in the file file into Easy CHM to generate the corresponding chm, put fanvicon.ico,
Your apache directory, Linux, he will automatically help you move, windows will not.
Chm fishing: https://422926799.github.io/2019/01/27/Chm-fishing/

By IX 2019/1/27

CVE-2018-18852是cerio路由器的CVE，github上有py2的，我这里写了个py3的

CVE-2018-18852 is the CVE of the cerio router, py2 on the github, I wrote a py3 here.

By 九世 2019/1/30

新增了一个子域名爆破，具体请看：https://422926799.github.io/2019/02/03/Subdomain-blasting/

Added a sub-domain blast, see: https://422926799.github.io/2019/02/03/Subdomain-blasting/

By 九世 2019/2/2

子域名爆破改进版，子域名爆破.rar那个

By 九世 2019/2/3

子域名爆破新增加了端口扫描和网页截图，不是rar的那个，适用于windows。如果Linux用户请自行下载Chrome的驱动和浏览器
扔到脚本目录，驱动下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads，指定端口扫描，不要把80和443去掉。

By 九世 2019/2/9

网易云下载那个是网易云音乐下载的进化版，可以搜索，下载，在线播放等应该说是打开浏览器自动播放

By 九世 2018/2/12

tuisec抓取，抓取某站点的安全热点，第一次先发送第一页全部，接下来每隔5秒获取更新的发送，若没有更新则不发送
发送邮箱推荐使用：搜狐邮箱
PS：发送的邮件如果收件箱是QQ邮箱的，会在垃圾箱里，请自行加入白名单

by 九世 2019/2/14


weblogic反序列化批量利用，可通过网页关键字判断是否weblogic服务，批量检测或单个检测，判断7001端口是否开放,可从zoomeye抓取IP，请自行配置config文件夹里面的search.ini，填写zoomeye的user和pwd。

by 九世 2019/2/16


ICMP远控是基于ICMP协议来进行互相交流通信的C2，需要安装scapy模块，至于打包成exe测试本人没成功= =。各位朋友自行测试，对了记得修改client.py和server.py的监听地址。这个我不想单独开个仓库来放，感觉写的烂。至于这个工具的原理，我会在我博客里面说，得等到星期六

by 九世 2019/2/27

jirb支持黑名单过滤，整个文件夹下的字典爆破，指定字典爆破，wordlist里面集成了dirb的字典和御剑与收集来的字典。爆破整个文件夹的下的字典时，config.ini default_file就设置为空，爆破指定文件的时候就反过来

by 九世 2019/3/5

psfvenom纯属闲着蛋疼写的，突然懒到连命令都不想打随便把几个常用的扔在了一起。方便快速生成

by 九世 2019/3/5

天眼查是我今天下午写来用于方便资产收集的脚本,遇见验证请手动打开URL绕过，自动过滤无网址的公司名称，默认爬5页

By 九世 2019/3/11

改进了RID劫持脚本，完全不靠命令进行修改

https://github.com/422926799/python/tree/master/RID%E5%8A%AB%E6%8C%81

By 九世 2019/3/26

朋友托我写几个awd的脚本给他，先从防御开始写吧，会持续更新

By 九世 2019/3/27

windows创建隐藏账户脚本

By 九世 2019/3/31

CVE-2019-3395和3396爆出来有几天了，几天抽了个时间写了一下，内带测试url
要更多的url的话
fofa搜:Confluence
zoomeye搜:app:"Confluence"

By 九世 2019/4/11

CVE定时更新，今天在看RSS的时候看到一篇文章说到了定时监控CVE更新

然后给出了一个接口：https://cassandra.cerias.purdue.edu/CVE_changes/today.html

这个接口每天会更新新的CVE，个人感觉不错索性爬了，会将抓到的详情CVE ur写入到以时间戳命名xls

By 九世 2019/4/14

简单的RAT的写的思路：https://422926799.github.io/posts/10e14164.html

By 九世 2019/4/20

CNVD-2019-48814利用工具是最近爆出来的weblogic反序列化RCE

详细文章可参考:https://www.jianshu.com/p/c4982a845f55


PS:漏洞编号好像打错了..CVE-2019-48814利用工具，CNVD-2019-48814


By 九世 2019/4/26

domain_query这个东东是用来批量查询子域名和爆破子域名的

参考文章:https://www.freebuf.com/vuls/198327.html

By 九世 2019/4/26



pirb目录探测工具，使用多进程+协程而写的，使用方法是

python3 pirb.py -u [url地址] -f [文件夹路径/] -s [匹配的状态码] -b [黑名单] -t [延时]

Usage: usage:[-u 地址] [-f 文件夹] [-s 匹配的状态码] 【- b 黑名单】 [-t 延时]

Options:
  -h, --help      show this help message and exit
  -u URL          指定目标url
  -f FILE         存放目录字典的文件夹
  -s STATUS_CODE  匹配指定的状态码
  -b BLACK        过滤掉黑名单里的字符
  -t SLEEPS       扫描延时

会过滤掉黑名单里面的内容，如果不匹配黑名单，请将黑名单留空

测试结果

图片地址:
https://s2.ax1x.com/2019/04/29/E3fEFO.md.png

https://s2.ax1x.com/2019/04/29/E3fQmt.png

https://s2.ax1x.com/2019/04/29/E3fwmq.png

By 九世 20119/4/29

写了个基于dns协议的远控，但是文件上传和文件下载有个BUG，至于怎么说我不清楚。总之不要上传或者下载那么大的东西
执行命令是没有任务问题的

使用AES加密，支持命令交互，文件上传，文件下载

 By 九世 2019/5/2
 
 
 勒索xxx模仿某安全情报所写，请勿做任何违法事件！
 
 By 九世 2019/5/6

写了个类似于Metasploit的框架，我想单独放在一个仓库
地址：https://github.com/422926799/Vulnerability_framework

By 九世 2019/5/11

写了个权限维持的脚本，叫做碧鳞蛇吧，详细用法请看
https://422926799.github.io/posts/91b15c6.html

    .---. .-.               .-.                        .-.         
: .; :: :               : :.-.                     : :.-.      
:   .': :   .--.   .--. : `'.'   .--. ,-.,-. .--.  : `'.' .--. 
: .; :: :_ ' .; ; '  ..': . `.  `._-.': ,. :' .; ; : . `.' '_.'
:___.'`.__;`.__,_;`.__.':_;:_;  `.__.':_;:_;`.__,_;:_;:_;`.__.'
    
[!] 该工具用于辅助权限维持，Thanks~

1.指定进程检测
2.开机自启添加
3.计划任务添加
4.启动文件夹添加
5.映像劫持
6.Winlogon registry entries注册表劫持
7.Applnit_DLLs劫持
8.创建恶意服务
9.服务劫持
Attack>

By 九世 2019/5/19

Four-Faith四口网路由器存活收集,早上看见某文章爆破四信的，顺便搞一下。填上zoomeye_username和zoomeye_password，页数可自己改，默认为10页。自动收集指定范围IP检测存在弱口令的IP，保存到save.txt

By 九世 2019/5/25

github搜索工具，可用于快速搜索github上的仓库。内有高级语法搜索与帮助

By 九世 2019/6/2


 _______         __ ________                    
|    ___|.-----.|__|  |  |  |.---.-.-----.-----.
|    ___||  -__||  |  |  |  ||  _  |     |  _  |
|___|    |_____||__|________||___._|__|__|___  |
                                         |_____|
                                         
接口搜索器_靡忘，用于搜索html源码里的js接口，使用无限爬虫
详细使用请看README.md

By 九世 2019/6/5


字典生成，可以指定生成密码的长度，从指定字符源里获取。配置文件在conf/config.ini里面
详情看文件夹里面的README.md

By 九世 2019/6/14


weblogic_poc利用是针对weblogic的CVE-2019-2725编号，进行批量的工具，具体看文件夹内的README.md

By 九世 2019/6/16

Windows系统安全事件应急响应那个文件夹里的脚本，是根据先知社区某文章提供的思路写的。可能不是很完善，望见谅。目的是更好的应急

By 九世 2019/6/23

twitter抓取是，用于抓取twitter里面指定用户的推文

By 九世 2019/6/29

新增一个信息收集工具，支持：
whois查询
端口扫描
C段查询
旁站查询
DNS查询
目录扫描
IP信息查询
web中间件程序查询
具体请看doc文件夹内的README.md

By 九世 2019/7/4


重新写了个爬补天项目大厅的工具，叫"补天"。具体怎么样你自己用用就知道了喔[滑稽]
By 九世 2019/7/8

新增一个百度采集器，获取：Server头，X-Forward-by头，title，url (原本是爬Google的，结果google把我恶心到了，有够逊的啦)
By 九世 2019/7/12

新增一个漏洞盒子自动提交漏洞工具
By 九世 2019/7/18
