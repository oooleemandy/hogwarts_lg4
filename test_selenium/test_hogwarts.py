'''
打开页面Testerhome
点击社团标签
点击求职面试圈
访问顶部第一个帖子
'''
from selenium import webdriver

class TestHogwarts():
    def setup(self):
        #初始化driver
        self.driver = webdriver.Chrome()
        #隐式等待，动态等待5秒。存在全局
        self.driver.implicitly_wait(5)
        #浏览器最大化
        self.driver.maximize_window()

    def teardown(self):
        #回收driver
        self.driver.quit()

    def test_hogwarts(self):
        #打开网址
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/div/div[1]/div[1]/"
                                          "div[2]/div[1]/a").click()


