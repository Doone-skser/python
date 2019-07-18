## 漏洞盒子自动提交漏洞 ##

- [x] 支持web类型随便提交
- [x] 支持批量提交


### 文件说明 ###
poc文件夹->里面放漏洞，请根据txt里面的格式来写
```
漏洞标题=说明2
漏洞类别=事件型漏洞
厂商信息=测试
所属域名=www.xxx2.com
漏洞类型=CSRF
漏洞等级=高危
漏洞描述=我只是测试批量提交漏洞的，审核爸爸放我一马吧= =
复现步骤=没有啊，别打我——，
图片=I:\jb\漏洞盒子自动提交漏洞\img\demo.jpg
图片=I:\jb\漏洞盒子自动提交漏洞\img\demo.jpg
修复方案=没有
匿名=是
漏洞url/位置=https://www.baidu.com/admin.php
影响参数=id
漏洞POC请求包=I:\jb\漏洞盒子自动提交漏洞\bug\poc.txt
```

tijiao.py
```python
username='username' #盒子账号
password='password' #盒子密码
id=1 #1为单个漏洞提交,2为批量漏洞提交
```

### 测试图 ###
![](https://s2.ax1x.com/2019/07/17/ZL97W9.gif)

# 本着提交漏洞更方便的愿景下开发这个工具，侵权请联系删除 #
