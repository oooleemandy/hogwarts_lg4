from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep

class TestTouchAction:
    def setup(self):
        '''设置w3c标准'''
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbutton(self):
        self.driver.get("https://www.baidu.com/")
        #定位到文本框
        el = self.driver.find_element_by_id("kw")
        #定位到搜索框
        el_search = self.driver.find_element_by_id("su")
        #对文本框中输入
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        #点击搜索
        action.tap(el_search)
        action.perform()

        #鼠标滑动，从el这个元素开始划，x轴偏移量为0，y轴偏移量越大越好，想划到底部
        action.scroll_from_element(el,0,10000).perform()
        # sleep(3)
