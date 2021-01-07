from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWX:
    def setup(self):
        '''复用浏览器，创建option。option制定浏览器启动debug地址。传进option'''
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)


    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        print(cookies)

