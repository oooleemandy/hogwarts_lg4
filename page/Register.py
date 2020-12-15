'''
注册页面
'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("填写企业名称")
        self.find(By.ID,"manager_name").send_keys("管理员姓名")
        return True