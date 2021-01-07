import os
from time import sleep
from selenium import webdriver

from test_pytest.base import Base


class TestWindow():
    def setup(self):
        #获取传过来的brower参数
        browser = os.getenv("browser")
        #判断browser参数
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换frame，找到”请拖拽我“这个元素所在的frame，用id取出
        self.driver.switch_to.frame("iframeResult")
        #打印”请推拽我“
        print(self.driver.find_element_by_id("draggable").text)


        #切换回默认frame,想去点击”点击运行“
        self.driver.switch_to.parent_frame()
        #或者
        #self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)

