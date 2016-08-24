#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
'''
Required
- requests (必须)
Info SmartQQ 2.0
- author : "slight"
- email  : "slight@fredom-sky.cc"
- date   : "2016.8.24"

'''
' SmartQQclient '

__author__ = 'Slight'



from time import *
import os
import re
import time
import sys
import subprocess
import requests
import json
import datetime
import random


class SmartQQclient(object):

    redirect_url = ''
    ptwebqq = ''
    vfwebqq = ''
    psessionid = ''
    clientid = 53999199
    uin = ''
    QRImgPath = ''

    headers = ''

    def __init__(self):
        global session
        global QRImgPath
        global screeningQQ

        self.QRImgPath = os.path.split(os.path.realpath(__file__))[0] + os.sep + 'webQQqr.jpg'
        self.session = requests.session()
        screeningQQ = [284438155]


    def ShowQRimage(self):
        global QRImgPath
        QRImgPath = self.QRImgPath
        url = 'https://ssl.ptlogin2.qq.com/ptqrshow'
        params = {
            'appid': 501004106,
            'e': 0,
            'l': 'M',
            's': 5,
            'd': 72,
            'v': 4,
            't': time.time()
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2774.3 Safari/537.36'
        }

        reponse = self.session.get(url, params=params, headers=headers  )
        # print(type(reponse))  >>> <class 'requests.models.Response'>
        with open(QRImgPath, 'wb') as f:
            f.write(reponse.content)
            f.close()
        #<-----linux可以直接注释掉-----
        if sys.platform.find('darwin') >= 0:
            subprocess.call(['open', QRImgPath])
        elif sys.platform.find('linux') >= 0:
            subprocess.call(['xdg-open', QRImgPath])
        else:
            os.startfile(QRImgPath)   
        #-----linux可以直接注释掉----->
        print('请使用手机QQ扫描二维码以登录')

    
    def WaitForlogin(self):
        global redirect_url
        global ptwebqq
        # 获取登录状态
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2774.3 Safari/537.36'
        }
        reponse = self.session.get(
            'https://ssl.ptlogin2.qq.com/ptqrlogin?webqq_type=10&remember_uin=1&login2qq=1&aid=501004106&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert&action=0-0-4190&mibao_css=m_webqq&t=undefined&g=1&js_type=0&js_ver=10151&login_sig=&pt_randsalt=0',
            headers=headers)
        # print reponse.cookies
        content = reponse.content.decode('utf-8')
        # print(content)
        # exit()
        res = re.search(r'ptuiCB(\(.*\))\;', content).group(1)
        res = eval(res)
        '''
        # 66:未失效 65:已失效  67:二维码认证中 0:登录成功
        # 0:
        return ptuiCB('0','0','http://ptlogin4.web2.qq.com/check_sig?pttype=1&uin=479531993&service=ptqrlogin&nodirect=0&ptsigx=f89bb6133db7b0438b8f62e73e84f370b7af02c43ae56e10cbbc175efce54e822fdbd45350356f9b27ce465535ac10ad9cd2195becd7d0f6c3218f5f2e14ce34&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&f_url=&ptlang=2052&ptredirect=100&aid=501004106&daid=164&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0','0','登录成功！', '阿新');
        '''
        code = res[0]
        print code
        if code == '67':
            print('成功扫描,请在手机上确认登录')
        elif code == '0':
            # 获取ptwebqq
            self.ptwebqq = reponse.cookies['ptwebqq']

            print('登录成功...')
            # 取出登录成功后的跳转地址
            self.redirect_url = res[2]
        elif code == '65':
            print('二维码失效,请重新启动程序')
        return code

   0