#author:九世
#time:2019/6/22
#file:windows_log.py

import os
import contextlib
import conf.config
from Evtx.Evtx import *
from Evtx.Views import *
import re
log_dict={}
def get_windows_login():
    dir=os.listdir('C:\Windows\System32\winevt\Logs')
    for i in dir:
        if i=='Application.evtx':
            log_dict['应用程序']='C:\\Windows\\System32\\winevt\\Logs\\'+i
        elif i=='System.evtx':
            log_dict['系统']='C:\\Windows\\System32\\winevt\\Logs\\'+i
        elif i=='Security.evtx':
            log_dict['安全']='C:\\Windows\\System32\\winevt\\Logs\\'+i
        elif i=='OAerts.evtx':
            log_dict['office']='C:\\Windows\\System32\\winevt\\Logs\\'+i
        elif i=='Windows PowerShell.evtx':
            log_dict['powershell']='C:\\Windows\\System32\\winevt\\Logs\\'+i

    for y in log_dict.keys():
        print('[+] windows日志:{}'.format(y))
        with open(log_dict[y],'r') as f:
            with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)) as buf: #内存映射处理
                fh=FileHeader(buf,0) #将二进制数据变成可视化xmla
                a=evtx_file_xml_view(fh)
                for xml,rec in a:
                    get_id(xml,conf.config.id)

def get_id(xml,id):
        global EventData
        ids=re.findall('<EventID Qualifiers="">.*</EventID>',xml)
        times=re.findall('<TimeCreated SystemTime=".*">',xml)
        EventData=re.findall('<Data Name=".*">.*</Data>',xml)
        if len(EventData)==0:
            EventData=''
        else:
            EventData="".join(EventData).replace('<Data','').replace('Name=','Name:').replace('"','').replace('<',' ').replace('/Data>','').replace('<',' ')

        for s in range(0,len(ids)):
            eventid=str(ids[s]).replace('<EventID Qualifiers="">','').replace('</EventID>','')
            event_time=str(times[s]).replace('<TimeCreated SystemTime=','').replace('"','').replace('>','')
            data = 'ID:{} 时间:{} EventData:{}'.format(eventid, event_time,EventData)
            if eventid in id:
                data = 'ID:{} 时间:{} 事件:{} EventData:{}'.format(eventid, event_time, id[eventid],EventData)
                print(data)
            else:
                print(data)