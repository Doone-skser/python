'''
author:九世
time:2019/7/16
fiel:tijiao.py
'''

from selenium import webdriver
from selenium.webdriver import *
import time
import os
import win32con
import win32gui
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

bug={} #漏洞信息
images=[] #存放要上传的图片
bug_tijiao=['bug_title']
tyon=[0,1] #漏洞类型设置,0为事件型漏洞,1为通用型漏洞
web_bug={'反射型XSS':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[1]/li[2]/a','存储型XSS':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[1]/li[3]/a','基于DOM型XSS':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[1]/li[4]/a'
         ,'其他类型XSS':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[1]/li[5]/a','SQL注入':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[2]/li[2]/a','命令注入':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[2]/li[3]/a'
         ,'CRLF注入':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[2]/li[4]/a','其他注入':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[2]/li[5]/a','逻辑漏洞':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[1]/a'
         ,'平行越权':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[3]/li[2]/a','垂直越权':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[3]/li[3]/a','其他权限控制缺失':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[3]/li[4]/a'
         ,'支付漏洞':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[2]/a','密码重置':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[4]/li[2]/a','任意注册':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[4]/li[3]/a'
         ,'任意登陆':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[4]/li[4]/a','撞库/扫号/暴力破解':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[4]/li[5]/a','其他认证缺陷':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[4]/li[6]/a',
         '弱口令':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[3]/a','条件竞争':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[4]/a','代码执行':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[5]/a'
         ,'信息泄露':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[6]/a','文件包含':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[7]/a','任意文件操作':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[8]/a'
         ,'上传漏洞':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[9]/a','URL重定向':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[10]/a','XXE':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[11]/a'
         ,'SSRF':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[12]/a','CSRF':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[13]/a','疑似入侵/存在后门':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[14]/a'
         ,'其他':'//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[15]/a'}

bug_level={'高危':'//*[@id="submitform"]/div[6]/div/div/div/ul/li[2]/a','中危':'//*[@id="submitform"]/div[6]/div/div/div/ul/li[3]/a','低危':'//*[@id="submitform"]/div[6]/div/div/div/ul/li[4]/a'} #漏洞级别

username='username' #盒子账号
password='password' #盒子密码
id=1 #1为单个漏洞提交,2为批量漏洞提交

chrome=webdriver.Chrome()
def login():
    chrome.get('https://account.tophant.com/login/') #进入登录界面
    chrome.implicitly_wait(5)
    input=chrome.find_element_by_name('username')
    input2=chrome.find_element_by_name('password')
    input3=chrome.find_element_by_id('loginBtn')
    input.send_keys(username)
    input2.send_keys(password)
    input3.click() #登录
    time.sleep(3)
    vulbox=chrome.find_element_by_class_name('img-noopen')
    vulbox.click()
    time.sleep(3)
    chrome.close() #关闭掉第一个标签页
    window=chrome.window_handles
    chrome.switch_to_window(window[0]) #切换到第二个标签页
    chrome.get('https://www.vulbox.com/user/submit-72') #进入到提交漏洞的url
    tijiao(chrome)

def tijiao(chrome):
    if id==1:
        hq=os.listdir('bug')
        dk=open('bug/{}'.format(hq[0]),'r',encoding='utf-8')
        read=dk.read()
        zz=re.findall('漏洞标题=.*',read)
        bug['漏洞标题']=str(zz[0]).replace('漏洞标题=','')
        zz1=re.findall('漏洞类别=.*',read)
        bug['漏洞类别'] = str(zz1[0]).replace('漏洞类别=', '')
        zz2=re.findall('厂商信息=.*', read)
        bug['厂商信息'] = str(zz2[0]).replace('厂商信息=', '')
        zz3 = re.findall('所属域名=.*', read)
        bug['所属域名'] = str(zz3[0]).replace('所属域名=', '')
        zz4 = re.findall('漏洞类型=.*', read)
        bug['漏洞类型'] = str(zz4[0]).replace('漏洞类型=', '')
        zz5 = re.findall('漏洞等级=.*', read)
        bug['漏洞等级'] = str(zz5[0]).replace('漏洞等级=', '')
        zz6 = re.findall('漏洞描述=.*', read)
        bug['漏洞描述'] = str(zz6[0]).replace('漏洞描述=', '')
        zz6 = re.findall('复现步骤=.*', read)
        bug['复现步骤'] = str(zz6[0]).replace('复现步骤=', '')
        zz6 = re.findall('修复方案=.*', read)
        bug['修复方案'] = str(zz6[0]).replace('修复方案=', '')
        zz7 = re.findall('匿名=.*', read)
        bug['匿名'] = str(zz7[0]).replace('匿名=', '')
        zz8 = re.findall('漏洞url/位置=.*', read)
        bug['漏洞url/位置'] = str(zz8[0]).replace('漏洞url/位置=', '')
        zz9 = re.findall('影响参数=.*', read)
        bug['影响参数'] = str(zz9[0]).replace('影响参数=', '')
        zz10 = re.findall('漏洞POC请求包=.*', read)
        bug['漏洞POC请求包'] = str(zz10[0]).replace('漏洞POC请求包=', '')



        img=re.findall('图片=.*',read)
        for it in img:
            images.append(str(it).replace('图片=',''))
        print(bug)
        chrome.find_element_by_name('bug_title').send_keys(bug['漏洞标题']) #填写漏洞标题
        if bug['漏洞类别']=='事件型漏洞': #设置漏洞类别
            leix=chrome.find_elements_by_name('bug_internet_type')[tyon[0]]
            leix.click()
        else:
            leix=chrome.find_elements_by_name('bug_internet_type')[tyon[1]]
            leix.click()

        chrome.find_element_by_name('bug_firm_name').send_keys(bug['厂商信息']) #填写厂商信息
        chrome.find_element_by_name('bug_firm_url').send_keys(bug['所属域名']) #所属域名
        chrome.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[1]/div').click() #点击漏洞类型的界面
        chrome.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[1]/a').click() #点击Web漏洞
        chrome.find_element_by_xpath(web_bug[bug['漏洞类型']]).click()
        chrome.find_element_by_xpath('//*[@id="submitform"]/div[6]/div/div/button').click() #点击漏洞级别的框框
        chrome.find_element_by_xpath(bug_level[bug['漏洞等级']]).click()
        chrome.find_element_by_xpath('//*[@id="submitform"]/div[8]/div/textarea').send_keys(bug['漏洞描述']) #漏洞描述
        chrome.find_element_by_xpath('//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[4]').send_keys(bug['复现步骤'])  # 填写复现步骤
        for tup in images:
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/a').click() #点击图片上传
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/div/ul/li[1]/a').click()
            time.sleep(1)
            dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'{}'.format(tup))  # 往输入框输入绝对地址
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[4]').send_keys(Keys.ENTER)

        chrome.find_element_by_xpath('//*[@id="submitform"]/div[17]/div/div/div[1]/div[4]').send_keys(bug['修复方案']) #填写修复方案
        if bug['匿名']=='否':
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[18]/div/div/div/div/span[3]').click()
        else:
            pass

        data=open(str(bug['漏洞POC请求包']),'r',encoding='utf-8').read()
        print(data)

        try:
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[9]/div/input').send_keys(bug['漏洞url/位置']) #填写漏洞URL
        except:
            pass

        try:
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[10]/div/input').send_keys(bug['影响参数']) #填写影响参数
        except:
            pass

        try:
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[11]/div').click()
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[11]/div/textarea').send_keys(data)
        except:
            pass

        #chrome.find_element_by_xpath('//*[@id="submit"]').click() #提交漏洞

    else:
        hq = os.listdir('bug')
        for v in hq:
            dk = open('bug/{}'.format(v), 'r', encoding='utf-8')
            read = dk.read()
            zz = re.findall('漏洞标题=.*', read)
            bug['漏洞标题'] = str(zz[0]).replace('漏洞标题=', '')
            zz1 = re.findall('漏洞类别=.*', read)
            bug['漏洞类别'] = str(zz1[0]).replace('漏洞类别=', '')
            zz2 = re.findall('厂商信息=.*', read)
            bug['厂商信息'] = str(zz2[0]).replace('厂商信息=', '')
            zz3 = re.findall('所属域名=.*', read)
            bug['所属域名'] = str(zz3[0]).replace('所属域名=', '')
            zz4 = re.findall('漏洞类型=.*', read)
            bug['漏洞类型'] = str(zz4[0]).replace('漏洞类型=', '')
            zz5 = re.findall('漏洞等级=.*', read)
            bug['漏洞等级'] = str(zz5[0]).replace('漏洞等级=', '')
            zz6 = re.findall('漏洞描述=.*', read)
            bug['漏洞描述'] = str(zz6[0]).replace('漏洞描述=', '')
            zz6 = re.findall('复现步骤=.*', read)
            bug['复现步骤'] = str(zz6[0]).replace('复现步骤=', '')
            zz6 = re.findall('修复方案=.*', read)
            bug['修复方案'] = str(zz6[0]).replace('修复方案=', '')
            zz7 = re.findall('匿名=.*', read)
            bug['匿名'] = str(zz7[0]).replace('匿名=', '')
            zz8 = re.findall('漏洞url/位置=.*', read)
            bug['漏洞url/位置'] = str(zz8[0]).replace('漏洞url/位置=', '')
            zz9 = re.findall('影响参数=.*', read)
            bug['影响参数'] = str(zz9[0]).replace('影响参数=', '')
            zz10 = re.findall('漏洞POC请求包=.*', read)
            bug['漏洞POC请求包'] = str(zz10[0]).replace('漏洞POC请求包=', '')

            img = re.findall('图片=.*', read)
            for it in img:
                images.append(str(it).replace('图片=', ''))
            print(bug)
            chrome.find_element_by_name('bug_title').send_keys(bug['漏洞标题'])  # 填写漏洞标题
            if bug['漏洞类别'] == '事件型漏洞':  # 设置漏洞类别
                leix = chrome.find_elements_by_name('bug_internet_type')[tyon[0]]
                leix.click()
            else:
                leix = chrome.find_elements_by_name('bug_internet_type')[tyon[1]]
                leix.click()

            chrome.find_element_by_name('bug_firm_name').send_keys(bug['厂商信息'])  # 填写厂商信息
            chrome.find_element_by_name('bug_firm_url').send_keys(bug['所属域名'])  # 所属域名
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[1]/div').click()  # 点击漏洞类型的界面
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[1]/a').click()  # 点击Web漏洞
            chrome.find_element_by_xpath(web_bug[bug['漏洞类型']]).click()
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[6]/div/div/button').click()  # 点击漏洞级别的框框
            chrome.find_element_by_xpath(bug_level[bug['漏洞等级']]).click()
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[8]/div/textarea').send_keys(bug['漏洞描述'])  # 漏洞描述
            chrome.find_element_by_xpath('//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[4]').send_keys(
                bug['复现步骤'])  # 填写复现步骤
            for tup in images:
                chrome.find_element_by_xpath(
                    '//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/a').click()  # 点击图片上传
                chrome.find_element_by_xpath(
                    '//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/div/ul/li[1]/a').click()
                time.sleep(1)
                dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
                ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
                ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
                Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
                button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
                win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'{}'.format(tup))  # 往输入框输入绝对地址
                win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
                chrome.find_element_by_xpath('//*[@id="submitform"]/div[15]/div/div[2]/div[1]/div[4]').send_keys(
                    Keys.ENTER)

            chrome.find_element_by_xpath('//*[@id="submitform"]/div[17]/div/div/div[1]/div[4]').send_keys(
                bug['修复方案'])  # 填写修复方案
            if bug['匿名'] == '否':
                chrome.find_element_by_xpath('//*[@id="submitform"]/div[18]/div/div/div/div/span[3]').click()
            else:
                pass

            data = open(str(bug['漏洞POC请求包']), 'r', encoding='utf-8').read()
            print(data)

            try:
                chrome.find_element_by_xpath('//*[@id="submitform"]/div[9]/div/input').send_keys(
                    bug['漏洞url/位置'])  # 填写漏洞URL
            except:
                pass

            try:
                chrome.find_element_by_xpath('//*[@id="submitform"]/div[10]/div/input').send_keys(bug['影响参数'])  # 填写影响参数
            except:
                pass

            try:
                chrome.find_element_by_xpath('//*[@id="submitform"]/div[11]/div').click()
                chrome.find_element_by_xpath('//*[@id="submitform"]/div[11]/div/textarea').send_keys(data)
            except:
                pass

            chrome.find_element_by_xpath('//*[@id="submit"]').click()  # 提交漏洞

            images.clear()
            bug.clear()
            time.sleep(30)
if __name__ == '__main__':
    login()