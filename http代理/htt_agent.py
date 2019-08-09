#@author:九世
#@time:2019/8/7
#@file:http_agent

import socket,threading,re,ssl

class Agent:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.request=[]
        self.timeout=3

    def http_request(self):
        global abt
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.host,self.port))
        s.listen(1)
        rqt=b''
        while True:
            abt,src=s.accept()
            dc=abt.recv(4096)
            self.http_header(dc)


    def http_header(self,request):
        if b'CONNECT' in request:
            host=str(re.findall('\s.*[:][0-9]{1,}',bytes(request).decode())[0]).lstrip().rstrip()
            port = str(re.findall('[:].*', host)[0]).replace(':', '').lstrip().rstrip()
            hosts = str(re.findall('.*[:]', host)[0]).replace(':', '').lstrip().rstrip()
            https = threading.Thread(target=self.https_get, args=(hosts, port, request))
            https.start()
        else:
            print('demo:{}'.format(request))
            try:
                #host=str(re.findall('Host[:] .*',bytes.decode(request,encoding='utf-8'))[0]).replace('\r','').replace('Host:','').lstrip().rstrip()
                host = bytes.decode(re.findall(b'Host[:] .*', request)[0]).replace('\r', '').replace('Host:','').lstrip().rstrip()
                if ':' in host:
                    port = str(re.findall('[:].*', host)[0]).replace(':', '').lstrip().rstrip()
                    host = str(re.findall('.*[:]', host)[0]).replace(':', '').lstrip().rstrip()
                else:
                    port = 80
                    host = host


                get = threading.Thread(target=self.http_get, args=(host, port, request))
                get.start()

            except:
                print('[Error]:获取host失败')



    def http_get(self,ip,port,request):
        print('连接:{}:{}'.format(ip,port))
        connects=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            connects.connect((ip,int(port)))
            connects.sendall(request)
            while True:
                response=connects.recv(4096)
                if response:
                    abt.sendall(response)
                else:
                    break

        except Exception as r:
            print('[Error]:{}'.format(r))

    def https_get(self,ip,port,request):
        print('https连接:{}:{}'.format(ip, port))
        connects = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connects.connect((ip,int(port)))
        t=threading.Thread(target=self.zx,args=(connects,))
        t.start()


    def zx(self,connects):
        reply = b"HTTP/1.1 200 Connection Established\r\n\r\n"  # requests模块用的是HTTP 1.0的协议 ,1.1的自己改
        abt.sendall(reply)  # 发给浏览器
        while True:
            jg=abt.recv(4096)
            if jg:
                t1=threading.Thread(target=self.zx2,args=(connects,jg))
                t1.start()
            else:
                break

    def zx2(self,connects,jg):
        connects.sendall(jg)
        jgs = connects.recv(4096)
        t2=threading.Thread(target=self.zx3,args=(abt,jgs))
        t2.start()

    def zx3(self,abt,jgs):
        abt.sendall(jgs)

if __name__ == '__main__':
    obj=Agent(host='127.0.0.1',port=4444)
    t=threading.Thread(target=obj.http_request,args=())
    t.start()