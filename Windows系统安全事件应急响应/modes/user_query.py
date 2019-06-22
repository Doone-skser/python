#author:九世
#time:2019/6/22
#file:user_query.py

import winreg
import binascii

def user_querys():
    dk_reg=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SAM\\SAM\\Domains\\Account\\Users\\Names')
    countkey=winreg.QueryInfoKey(dk_reg)[0]
    users=[]
    users_f=[]
    userid=[]
    for k in range(int(countkey)):
        name=winreg.EnumKey(dk_reg,k)
        users.append(name)
    winreg.CloseKey(dk_reg)

    for u in users:
        ud=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SAM\\SAM\\Domains\\Account\\Users\\Names\\{}'.format(u))
        fd=winreg.QueryValueEx(ud,'')
        users_f.append(fd[1])
        winreg.CloseKey(ud)

    for f in users_f:
        usid=str(hex(f)).replace('0x','00000')
        ug=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SAM\\SAM\\Domains\\Account\\Users\\{}'.format(usid))
        user_F=winreg.QueryValueEx(ug,'F')
        userid.append(bytes.decode(binascii.hexlify(user_F[0])))

    print('[!] 小贴士:当用户管理员的用户权限出现在其他用户里面，代表攻击者执行了RID劫持。对比net user下得到的用户名和本程序得到的用户名，如果不相同则，存在隐藏用户')
    for j in range(0,len(users)):
        data='用户名:{} 用户ID:{} 用户权限设置:{}'.format(users[j],users_f[j],userid[j])
        print(data)