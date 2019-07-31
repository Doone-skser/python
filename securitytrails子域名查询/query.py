#@:author:九世
#@:time:2019/7/31
#@:file:query.py

import requests
import json

class Query:
    def __init__(self,domain):
        self.domain=domain
        self.headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                      'accept': 'application/json',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://securitytrails.com',
                'referer': 'https://securitytrails.com/list/apex_domain/{}'.format(domain)}
        self.data={
            '_csrf_token': "EBQgAHl8TD5kIQZ0NwQ1GjwUGDpLNgAAyBpa029G1FPGT5dbTrbJdw=="
        }
        self.cookies={}
        self.cookie='_ga=GA1.2.398527090.1562894978; _vwo_uuid_v2=DB07ADE57B1FF5BF27E72AABC7DB0AA9A|a8dafd81a34d7561d8f62bc56f5fd9bd; driftt_aid=e2732d1c-6343-4900-a39d-d31f156ecf78; _vwo_uuid=DB07ADE57B1FF5BF27E72AABC7DB0AA9A; __adroll_fpc=a257f67df9b64a68a3813163f0d44487-s2-1562895001263; DFTT_END_USER_PREV_BOOTSTRAPPED=true; _fbp=fb.1.1562900542407.1027035832; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241562894984%3A79.9268242%3A%3A%3A21_0%2C12_0%2C11_0%2C3_0%3A0; _gid=GA1.2.1816985868.1564556025; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; driftt_sid=6fab05cf-1896-464d-bd1b-38575cf077c5; mp_679f34927f7b652f13bda4e479a7241d_mixpanel=%7B%22distinct_id%22%3A%20%22u_cbffded5-1f17-456d-9a34-b47f909d79d9%22%2C%22%24device_id%22%3A%20%2216be3cd1e89a9-04685e963cfc2a-39395704-1fa400-16be3cd1e8a520%22%2C%22app%22%3A%20%22SecurityTrails%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20%22st-app%22%2C%22utm_medium%22%3A%20%22cta-bottom%22%2C%22%24user_id%22%3A%20%22u_cbffded5-1f17-456d-9a34-b47f909d79d9%22%7D; _vwo_sn=1661044%3A3; _securitytrails_app=QTEyOEdDTQ.xAEH7gd3mq9J3KotfdnbrBE71aIoo1ggTlfrQ7zmBS6PU0-VGvKLALDHPCM._K2ek54ZgrLh891T.55Apss4BHtOa0LLMsyfBaxd0qKMhTXhOa1rW-YQGmrChdSCc3ladU0h3193RdWqiS7eKK5AAw1EgZ641XqPs3-wYwxW6AqpTohGvxgsWJQ.jOvOl2CsGBWBqNo9enJCvA; __ar_v4=GDFF5LAGC5AWTKDNHLCMI5%3A20190711%3A8%7CK4MIVIZDAZFQJNYFCCLGOP%3A20190711%3A8%7CDISBUDHYAZAKNC7GVZRXHU%3A20190711%3A8'
        for s in self.cookie.split(';'):
            key,value=s.split('=',1)
            self.cookies[key]=value

    def request(self):
        page=1
        while True:
            page+=1
            url = ' https://securitytrails.com/app/api/v1/list?page={}&apex_domain={}'.format(page,self.domain)
            rqt=requests.post(url=url,headers=self.headers,data=json.dumps(self.data),cookies=self.cookies)
            if not 'records' in rqt.text:
                break
            jsons=rqt.json()['records']
            for d in jsons:
                domain=d['hostname']
                print(domain)
                print(domain,file=open('save.txt','a'))