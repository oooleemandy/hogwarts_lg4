from time import sleep

from selenium.webdriver import ActionChains

from test_pytest.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换frame，找到”请拖拽我“这个元素所在的frame，用id取出
        self.driver.switch_to.frame("iframeResult")

        #找到要拖拽的两个元素
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")

        action = ActionChains(self.driver)
        #需要把drag拖拽到drop中
        action.drag_and_drop(drag,drop).perform()
        sleep(3)


        '''
        拖拽完以后会有弹框，需要切换到弹框页面再点击确认
        '''
        self.driver.switch_to.alert.accept()


        '''
        alert点击确认后再返回到默认的frame下,然后点击运行
        '''
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)


