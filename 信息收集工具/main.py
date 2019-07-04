# @author:九世
# @time:2019/7/2
# @file:mian.py

from gevent import monkey
monkey.patch_all()
import config.config
import modular.registration_information
import modular.Real_IP
import modular.Port_Scanning
import config.config
import modular.dns_query
import modular.Subdomain_name_query
import modular.Directory_detection
import modular.web_jianc
import threading
import time

lock=threading.RLock()

def loggin():
    def wt(func):
        def jilu(*args,**kwargs):
            print('\033[1;34m[loggin]\033[0m run function:{}'.format(func.__name__))
            return func(*args,**kwargs)
        return jilu
    return wt

class shouji():
    def run(self):
        domain=config.config.DOMAIN
        url=config.config.URL
        thread=[]
        thread.append(threading.Thread(target=self.whois_query,args=(domain,)))
        thread.append(threading.Thread(target=self.IP_query,args=(domain,)))
        thread.append(threading.Thread(target=self.dnsquery,args=(domain,)))
        thread.append(threading.Thread(target=self.subdomain_query,args=(domain,)))
        thread.append(threading.Thread(target=self.port_scan,args=(domain,)))
        thread.append(threading.Thread(target=self.Directory_detection,args=(config.config.URL,)))
        thread.append(threading.Thread(target =self.web_jianc,args=(url,)))

        for t in thread:
            t.start()
            t.join()
            time.sleep(1)

    @loggin()
    def whois_query(self,url):
        lock.acquire()
        modular.registration_information.run(url)
        lock.release()

    @loggin()
    def IP_query(self,url):
        lock.acquire()
        modular.Real_IP.run(url)
        lock.release()

    @loggin()
    def port_scan(self,url):
        lock.acquire()
        modular.Port_Scanning.run(url)
        lock.release()

    @loggin()
    def dnsquery(self,url):
        lock.acquire()
        modular.dns_query.run(url)
        lock.release()

    @loggin()
    def subdomain_query(self,url):
        lock.acquire()
        if config.config.DOMAIN_BAOPO==0:
            modular.Subdomain_name_query.run(url)
            modular.Subdomain_name_query.cat()
        elif config.config.DOMAIN_BAOPO==1:
            modular.Subdomain_name_query.run(url)
            modular.Subdomain_name_query.run2(url)
            modular.Subdomain_name_query.cat()
        lock.release()


    @loggin()
    def Directory_detection(self,url):
        modular.Directory_detection.scan(url)

    @loggin()
    def web_jianc(self,url):
        modular.web_jianc.web_server_shibie(url)
        modular.web_jianc.error_jiance(url)

if __name__ == '__main__':
    obj=shouji()
    obj.run()
