#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from podemo1.page.base_page import BasePage

class AddMemberPage(BasePage):

    '''添加联系人操作'''
    def add_member(self, name, account, phonenum):
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True


    '''判断联系人是否添加成功'''
    def get_member(self, value):
        '''调用显示等待方法，查看checkbok是否可被点击，可被点击说明页面加载完成了'''
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator)


        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        '''列表推导式，在element中获取title属性'''
        titles = [element.get_attribute("title") for element in elements]

        return titles