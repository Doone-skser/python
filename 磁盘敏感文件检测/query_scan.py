'''
Find sensitive files on disk
'''
import os
import re

class Search:
    def __init__(self):
        self.cipan=[]
        self.cioan=[]
        self.paths=[]
        self.calc=0
        self.chi=['config','敏感','机密','绝密','username','password','密码','账号','version','名单','公司','人际']
        for j in range(65,91):
            self.cipan.append(chr(j))

    def query(self):
        for gb in self.cipan:
            if os.path.exists('{}:'.format(gb)):
                self.cioan.append('{}:\\'.format(gb))

        for p in self.cioan:
           for jg in  self.huoqu(p):
               print(jg)



    def huoqu(self,path):
        for r in os.walk(path):
            for g in r[1:]:
                for name in g:
                    self.paths.append('{}\\{}'.format(r[0],name))

        for g in self.chi:
            for w in self.paths:
                if g in w:
                    mg='发现敏感文件 路径:{} 关键词:{}'.format(w,g)
                    yield mg

if __name__ == '__main__':
    obj=Search()
    obj.query()