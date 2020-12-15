'''
建模登陆页面,一共两个功能，扫描和进入注册页面
'''
from selenium.webdriver.common.by import By

from page.Register import Register
from page.base_page import BasePage


class Login(BasePage):
    #扫码方法
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)
