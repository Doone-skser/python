#author:九世
#time:2019/6/22
#file:zhu.py

import os

usage=['1.查看windows日志','2.查看windows用户名','3.查看网络连接','4.防火墙的配置','5.进程信息','6.内存dump的路径','7.获取开机启动的信息','8.获取所有服务的信息','9.计划任务下的文件信息','10.获取最近的访问的文件','11.执行上述所有操作']

class Main:
    #检查模块文件是否存在
    def modes_file(self,id):
        global exc
        exc = {'1':self.windows_log,'2':self.windows_user_query,'3':self.port_open,'4':self.netsh_conf,'5':self.jinc,'6':self.dump_file,'7':self.boot_run,'8':self.services_query,'9':self.thasks_query,'10':self.recent,'11':self.run_all}
        if os.path.exists('modes'):
            print('[+] 找到插件文件夹')
            if id in exc:
                try:
                    exc[id]()
                except Exception as r:
                    if 'Permission' in str(r) or '拒绝访问' in str(r):
                        print('[!] 权限不足,请以Administrator权限，访问此脚本')
        else:
            print('[-] 找不到插件文件夹')
            exit()
    #获取windows日志
    def windows_log(self):
        print('[+] 加载windows日志获取模块....')
        windows_logs=__import__('modes.windows_log',fromlist=True)
        get=getattr(windows_logs,'get_windows_login')
        get()

    #获取windows用户名
    def windows_user_query(self):
        print('[+] 加载windows用户获取模块...')
        windows_users=__import__('modes.user_query',fromlist=True)
        get=getattr(windows_users,'user_querys')
        get()

    #获取网络连接
    def port_open(self):
        print('[+] 加载服务信息获取模块...')
        network_connect=__import__('modes.service_query',fromlist=True)
        get=getattr(network_connect,'portopen')
        get()

    #获取防火墙的配置
    def netsh_conf(self):
        print('[+] 加载服务信息获取模块...')
        netshs=__import__('modes.service_query',fromlist=True)
        get=getattr(netshs,'netshs')
        get()

    #获取进程信息
    def jinc(self):
        print('[+] 加载服务信息获取模块...')
        jincs = __import__('modes.service_query', fromlist=True)
        get = getattr(jincs, 'jinc')
        get()

    #获取dumpfile的路径
    def dump_file(self):
        print('[+] 加载dump_file路径搜索模块...')
        dump_path=__import__('modes.memory_dump',fromlist=True)
        get=getattr(dump_path,'inspect')
        get()

    #获取开机自启的信息
    def boot_run(self):
        print('[+] 加载开机启动信息收集模块...')
        boot_runs=__import__('modes.bootup_run',fromlist=True)
        get=getattr(boot_runs,'boot_runquery')
        get()

    #获取所有服务信息
    def services_query(self):
        print('[+] 加载获取服务信息的模块...')
        services=__import__('modes.services_query',fromlist=True)
        get=getattr(services,'hq')
        get()

    #计划任务下的文件信息
    def thasks_query(self):
        print('[+] 加载获取计划任务信息的模块...')
        schtasks=__import__('modes.schtasks_query',fromlist=True)
        get=getattr(schtasks,'jiancha')
        get()

    #获取最近的访问的文件
    def recent(self):
        print('[+] 加载获取最近访问文件的模块...')
        rant=__import__('modes.recent_query',fromlist=True)
        get=getattr(rant,'hq')
        get()

    def run_all(self):
        for j in exc:
            try:
                exc[j]()
            except Exception as r:
                if 'Permission' in str(r) or '拒绝访问' in str(r):
                    print('[!] 权限不足,请以Administrator权限，访问此脚本')

if __name__ == '__main__':
    obj=Main()
    for u in usage:
        print(u)
    print('')
    user=input('要执行的ID:')
    obj.modes_file(user)
