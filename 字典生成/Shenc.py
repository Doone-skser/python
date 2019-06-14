'''
author:九世
time:2019/6/14
file:Sehnc.py
'''
import os
import configparser
import random
import re

configs={}
data=['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','x','u','v','w','z']

class Sehnc:
    def __init__(self,path):
        self.path=path


    def config(self):
        if os.path.exists(self.path):
            print('[+] 配置文件存在')
            cf=configparser.ConfigParser()
            cf.read(self.path)
            configs['number']=cf.get('dict_shengc','number')
            configs['character']=cf.get('dict_shengc','character')
        else:
            print('[-] 找不到配置文件')
            exit()

    def shenc(self):
        ac='.format('
        calc=''
        j=0
        calcs='print("'
        none=''
        nb=int(configs['number'])
        for i in range(nb):
            rd = random.choice(data)
            if j==1:
                none+=' '
            rd='{}{}'.format(rd,j)
            r = "{}for {} in configs['character']:\n".format(none,rd)
            calc+=r
            none*=2
            j+=1


        zz=re.findall('[a-z][0-9] in',calc)
        for z in zz:
            ac+=str(z).replace('in','').rstrip()
            ac+=','
            calcs+='{}'
        calcs += '"'
        ac+=')'
        ac=ac[0:-2]
        ac+=')'
        calc+=none+calcs+ac+')'
        exec (calc)

if __name__ == '__main__':
    path='conf/config.ini'
    obj=Sehnc(path=path)
    obj.config()
    obj.shenc()