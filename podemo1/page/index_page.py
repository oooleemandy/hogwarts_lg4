#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from podemo1.page.addmemberpage import AddMemberPage
from podemo1.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#"

    def click_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)