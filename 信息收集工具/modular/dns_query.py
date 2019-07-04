# @author:九世
# @time:2019/7/2
# @file:mian.py

import dns.resolver

lei=['A','CNAME','MX','TXT','SRV','']

def query():
    def wrt(func):
        def qt(*args,**kwargs):
            for l in lei:
                print('\033[1;32m[+]\033[0m 域名:{} 类型:{}'.format(*args,l))
                try:
                    result=dns.resolver.query(*args,'{}'.format(l))
                    for j in result:
                        print(j)
                except Exception as r:
                    print(r)
            return func(*args,**kwargs)
        return qt
    return wrt

@query()
def run(url):
    pass