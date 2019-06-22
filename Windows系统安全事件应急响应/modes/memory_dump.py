#author:九世
#time:2019/6/22
#file:memory_dump.py

import winreg

#检查DMP文件的路径
def inspect():
    jianc=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SYSTEM\\ControlSet002\\Control\\CrashControl')
    memory_path=winreg.QueryValueEx(jianc,'DumpFile')
    print('[+] dump_file路径:{}'.format(memory_path[0]))