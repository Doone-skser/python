### 信息收集工具_Shadow spider ###
- [x] whois查询
- [x] 网站真实IP
    + IP信息 
    + 是否有CDN

- [x] 端口扫描
- [x] dns记录
- [x] 子域名
    + 爬子域名查询的站点
    + 爆破子域名
   
- [x] 目录探测
- [x] C段和旁站收集
- [x]  web中间件信息收集
- [x] web错误信息检测

### 需要安装的第三方模块 ###
```txt
whois
requests
bs4
dns
gevent
multiprocessing
IPy
```

测试效果如下：
```txt
[loggin] run function:whois_query
[+] 查询结果:xkb.com.au
{
  "domain_name": "XKB.COM.AU",
  "last_modified": "2018-10-25T06:53:38Z",
  "registrar": "Synergy Wholesale Pty Ltd",
  "status": "serverRenewProhibited https://afilias.com.au/get-au/whois-status-codes#serverRenewProhibited",
  "registrant_name": "KINGOLD MEDIA (AUST) PTY LTD",
  "name_servers": [
    "NS7.ALIDNS.COM",
    "NS8.ALIDNS.COM"
  ]
}
[loggin] run function:IP_query
[+] 真实IP:119.9.35.129
[+]IP详细信息:香港特别行政区  参考数据1：澳大利亚新南威尔士州悉尼  rackspace.com参考数据2：中国兼容IPv6地址：::7709:2381映射IPv6地址：::FFFF:7709:2381
[+] 旁站查询
没有查询到旁站信息
[+] C段查询
IP:119.9.35.46----站点:<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>502 - Web server received an invalid response while acting as a gateway or proxy server.</title>
<style type="text/css">
<!--
bodymargin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;
fieldsetpadding:0 15px 10px 15px; 
h1font-size:2.4em;margin:0;color:#FFF;
h2font-size:1.7em;margin:0;color:#CC0000; 
h3font-size:1.2em;margin:10px 0 0 0;color:#000000; 
#headerwidth:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;
background-color:#555555;
#contentmargin:0 0 0 2%;position:relative;
.content-containerbackground:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;
-->
</style>
</head>
<body>
<div id="header"><h1>Server Error</h1></div>
<div id="content">
 <div class="content-container"><fieldset>
  <h2>502 - Web server received an invalid response while acting as a gateway or proxy server.</h2>
  <h3>There is a problem with the page you are looking for, and it cannot be displayed. When the Web server (while acting as a gateway or proxy) contacted the upstream content server, it received an invalid response from the content server.</h3>
 </fieldset></div>
</div>
</body>
</html>

IP:119.9.35.98----站点:<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>502 - Web server received an invalid response while acting as a gateway or proxy server.</title>
<style type="text/css">
<!--
bodymargin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;
fieldsetpadding:0 15px 10px 15px; 
h1font-size:2.4em;margin:0;color:#FFF;
h2font-size:1.7em;margin:0;color:#CC0000; 
h3font-size:1.2em;margin:10px 0 0 0;color:#000000; 
#headerwidth:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;
background-color:#555555;
#contentmargin:0 0 0 2%;position:relative;
.content-containerbackground:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;
-->
</style>
</head>
<body>
<div id="header"><h1>Server Error</h1></div>
<div id="content">
 <div class="content-container"><fieldset>
  <h2>502 - Web server received an invalid response while acting as a gateway or proxy server.</h2>
  <h3>There is a problem with the page you are looking for, and it cannot be displayed. When the Web server (while acting as a gateway or proxy) contacted the upstream content server, it received an invalid response from the content server.</h3>
 </fieldset></div>
</div>
</body>
</html>

IP:119.9.35.128----站点:﻿"domain":"http://www.xkb.com.au","title":"","domain":"http://xkb.com.au","title":""
IP:119.9.35.166----站点:﻿"domain":"http://www.fernland.com.au","title":""
[loggin] run function:dnsquery
[+] 域名:xkb.com.au 类型:A
119.9.35.129
[+] 域名:xkb.com.au 类型:CNAME
The DNS response does not contain an answer to the question: xkb.com.au. IN CNAME
[+] 域名:xkb.com.au 类型:MX
10 xkb-com-au.mail.protection.outlook.com.
[+] 域名:xkb.com.au 类型:TXT
"google-site-verification=bV3pgyMJbQaX-TPAQ8YmBAwLk3YKDvz0WzRU-kK1XkI"
"v=spf1 include:spf.protection.outlook.com -all"
[+] 域名:xkb.com.au 类型:SRV
The DNS response does not contain an answer to the question: xkb.com.au. IN SRV
[+] 域名:xkb.com.au 类型:
DNS resource record type is unknown.
[loggin] run function:subdomain_query
[+] 域名查询:
www.xkb.com.au
xkb.com.au
[loggin] run function:port_scan
[loggin] run function:Directory_detection
[+] 找到以下路径：
https://xkb.com.au//robots.txt
[loggin] run function:web_jianc
[+] web程序中间件信息
nginx/1.10.2
[+] 站点404错误信息
<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.10.2</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
[+] 443/Open banner:HTTP/1.1 400 Bad Request
Server: nginx/1.10.2
Date: Thu, 04 Jul 2019 02:33:49 GMT
Content-Type: text/html
Content-Length: 173
Connection: close

<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.10.2</center>
</body>
</html>

[+] 80/Open banner:HTTP/1.1 400 Bad Request
Server: nginx/1.10.2
Date: Thu, 04 Jul 2019 02:34:29 GMT
Content-Type: text/html
Content-Length: 173
Connection: close

<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.10.2</center>
</body>
</html>

https://xkb.com.au//plus/flink_add.php
https://xkb.com.au//plus/flink.php
https://xkb.com.au//plus/stow.php
https://xkb.com.au//include/helpers/archive.helper.php
https://xkb.com.au//data/admin/config_update.php
https://xkb.com.au//m/index.php
https://xkb.com.au//plus/vote.php
https://xkb.com.au//tags.php
https://xkb.com.au//favicon.ico
https://xkb.com.au/m/
https://xkb.com.au//include/taglib/adminname.lib.php
https://xkb.com.au//plus/list.php
https://xkb.com.au//plus/view.php
https://xkb.com.au//plus/mytag_js.php
https://xkb.com.au//index.html
https://xkb.com.au//index.html
https://xkb.com.au//plus/disdls.php
https://xkb.com.au//plus/feedback_js.php
https://xkb.com.au//robots.txt
https://xkb.com.au//plus/erraddsave.php
https://xkb.com.au//data/admin/ver.txt
https://xkb.com.au//favicon.ico
https://xkb.com.au/special/
https://xkb.com.au//plus/feedback_ajax.php
https://xkb.com.au//upload/../robots.txt
https://xkb.com.au//robots.txt
https://xkb.com.au//include/memberlogin.class.php
```