#author:九世
#time:2019/6/22
#file:services_query.py

import winreg

service_name=[]

def hq():
    dk_key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SYSTEM\\ControlSet002\\services')
    info_key=winreg.QueryInfoKey(dk_key)[0]
    for c in range(int(info_key)):
        hj=winreg.EnumKey(dk_key,c)
        service_name.append(hj)

    winreg.CloseKey(dk_key)

    for name in service_name:
        print('[+] 服务名:{}'.format(name))
        dk2_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\ControlSet002\\services\\{}'.format(name))
        try:
            calc=0
            while True:
                name,value,type=winreg.EnumValue(dk2_key,calc)
                print('名称:{} 值:{} 类型:{}'.format(name,value,type))
                calc+=1
        except:
            pass

        print('')