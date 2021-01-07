from time import sleep

from test_pytest.base import Base


class TestFile(Base):
    def test_file(self):
        '''
        1、进入百度图库首页
        2、点击加图片按钮

        '''
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("uploadImg").send_keys(r"C:\Users\limandi\PycharmProjects\hogwarts_lg4\image\Screenshot.jpg")
        sleep(3)