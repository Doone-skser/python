# @author:九世
# @time:2019/7/8
# @file:config.py

COOKIE='This is your cookie'
PAGE=20 #公益页数你尽管设，专属只有一页只能设1，企业也是
PROCESS=100 #协程设置
VERSION=0.1
ID={1:'/Reward/pub',2:'/Reward/corps',3:'/Reward/com'} #1为抓取公益SRC,2为专属SRC,3为企业SRC
SET_ID=1 #ID设置
WAIT=0.3 #遇见验证码的等待时间
URL='https://www.butian.net' #补天的URL
LOOK_ID='https://www.butian.net/Loo/submit?cid={}' #获取域名的url