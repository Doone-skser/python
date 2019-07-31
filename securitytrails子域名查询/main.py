#@:author:九世
#@:time:2019/7/31
#@:file:found.py

import found
import query
import reqts
import os

class Main:
    def __init__(self):
        print('[= =] 欢迎使用子域名一条龙信息收集工具')
        if os.path.exists('save.txt'):
            print('---已找到save.txt,开启暴躁的信息采集---')
            fd=found.Found()
            fd.djc()
            print('---暴躁的信息采集2---')
            rqts=reqts.Rgbtsqeury()
            rqts.djc()
        else:
            print('[- -] 没有检测到save.txt,开启暴躁的子域名查询')
            users=input('[- -] 要查询的域名>')
            qt=query.Query('{}'.format(users))
            qt.request()
            Main()

if __name__ == '__main__':
    obj=Main()
