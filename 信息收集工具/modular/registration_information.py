# @author:九世
# @time:2019/7/2
# @file:mian.py

import whois

def query():
    def fuc(func):
        def wtr(*args,**kwargs):
            qt=whois.whois(*args)
            print('\033[1;32m[+]\033[0m 查询结果:{}'.format(*args))
            print(qt)
            return func(*args,**kwargs)
        return wtr
    return fuc

@query()
def run(url):
    pass