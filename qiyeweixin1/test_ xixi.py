#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        option = Options()
        # 注意 9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False,
             'value': 'o0137787592'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1641444557.818233, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False,
             'value': '@2J2LvbQDD'},
            {'domain': '.qq.com', 'expiry': 2147483430.511013, 'httpOnly': False, 'name': 'RK', 'path': '/',
             'secure': False, 'value': 'JMJcSTgSG7'},
            {'domain': '.qq.com', 'expiry': 2147483430.511117, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
             'secure': False, 'value': '0c1a882cad52a4cbc5005d9fc4854a9ca4021eb49f19f142d1c2ae1dce46acc0'},
            {'domain': '.qq.com', 'expiry': 1673079672, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1128381225.1609908570'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1641532590, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609908568'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1612600110.970827, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '03184142'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1609996590'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1610028127.526147, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '3kc9kf'},
            {'domain': '.qq.com', 'expiry': 1610094072, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.188972918.1609996592'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324943175019'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688854068709900'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688854068709900'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7660320'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'HGCZDgTSb3atjZZild4lXv7CS-1WJd5q6Skr1MC62vfiPHMZf4S1UGLYNAU301mZ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'dQYK81YHVde8EyIoPwvIXSvU4yXdODUSwoohTNR7WAX3xkvlu9E0Jmql5J4B_NA-Vylr4BPeULXITZXXxAdTweWloLFu8ovEE5rXMPcfQHfx_q7yNhAdjqrugW0y36Jf14PQEmCTVWq3NjNoI06ge899qe6yDloCS0fKj0COgZ1EFJm--9uW1F0dQKFpAIKSY9bbE41sQv5Y_jkjkFG0MiSEfrrqH33Drf1faVGArQ-QSYL18ctF3OAcwfyVsOr6qhulnU7Os9jQqjhMwY0gpw'}
        ]
        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_import_contacts(self):
        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        # 点击【导入联系人】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        sleep(5)

        cookies = [
            {'domain': '.work.weixin.qq.com', 'expiry': 1612615175.352724, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1641559174.095903, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1610054710.095798, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '2afftht'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '02601473'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        '''以上cookie列表中有多个字典，for循环遍历列表，让每一个字典都放进'''
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")