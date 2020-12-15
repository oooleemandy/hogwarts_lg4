'''
企业微信首页
主页功能：登陆 注册
'''
from selenium.webdriver.common.by import By

from page.Login import Login
from page.Register import Register
from page.base_page import BasePage


class Main(BasePage):
    #声明base url,子类里重写url
    _base_url = "https://work.weixin.qq.com/"

    #goto注册页面
    def goto_register(self):
        #复制的是class，”.“代表class
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)
    #goto登陆页面
    def goto_login(self):
        #点击登陆
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        #进入到注册页
        return Login(self._driver)
