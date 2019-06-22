#windows事件id
id={
'2':'交互式登录（用户从控制台登录）',
'3':'网络（例如：通过net use, 访问共享网络）',
'4':'批处理（为批处理程序保留）',
'5':'服务启动（服务登录）',
'6':'不支持',
'7':'解锁（带密码保护的屏幕保护程序的无人值班工作站）',
'8':'网络明文（IIS服务器登录验证）',
'10':'远程交互（终端服务，远程桌面，远程辅助）',
'11':'缓存域证书登录',
'1102':'清理审计日志',
'4624':'账号成功登录',
'4648':'使用明文凭证尝试登录',
'4625':'账号登录失败',
'4768':'Kerberos身份验证（TGT请求）',
'4769':'Kerberos服务票证请求',
'4776':'NTLM身份验证',
'4672':'授予特殊权限',
'4720':'创建用户',
'4726':'删除用户',
'4728':'将成员添加到启用安全的全局组中',
'4729':'将成员从安全的全局组中移除',
'4732':'将成员添加到启用安全的本地组中',
'4733':'将成员从启用安全的本地组中移除',
'4756':'将成员添加到启用安全的通用组中',
'4757':'将成员从启用安全的通用组中移除',
'4719':'系统审计策略修改',
'4778':'重新连接到一台 Windows 主机的会话',
'4779':'断开到一台 Windows 主机的会话'
}

#查找出特定的端口号,没有请留空
port=''

#查找指定PID,没有请留空
pid=''


#开启启动注册表检测路径
path={
'"HKLM\Software\Microsoft\Windows\CurrentVersion\Runonce"',
'"HKLM\Software\Microsoft\Windows\CurrentVersion\policies\Explorer\Run"',
'"HKLM\Software\Microsoft\Windows\CurrentVersion\Run"',
'"HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Run"',
'"HKCU\Software\Microsoft\Windows\CurrentVersion\Run"',
'"HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce"'
}

#计划任务文件夹的配置
tasks_path={
'C:\\Windows\\System32\Tasks\\',
'C:\\Windows\\SysWOW64\Tasks\\',
'C:\\Windows\\tasks\\'
}