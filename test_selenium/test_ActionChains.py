import pytest
from selenium  import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #分别拿到单击、双击、右键元素
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")

        #创建action方法
        action = ActionChains(self.driver)
        #分别创建单击、右键、双击方法
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)

        #执行action
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        #找到设置
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        #光标移动到设置上
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)

        #拖拽
        # action.drag_and_drop(drag_element,drop_element).perform()

        #点击某个元素然后释放某个元素
        # action.click_and_hold(drag_element).release(drop_element).perform()

        #点击某个元素不放，然后moveto到某个元素上
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()

        action = ActionChains(self.driver)
        #输入文字
        action.send_keys("username").pause(1)
        #输入空格
        action.send_keys(Keys.SPACE).pause(1)
        #再输入文字
        action.send_keys("tom").pause(1)
        #操作回删
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)