'''
打开测试人网站
点击分类
查看“最新“是否出现
如果出现了就点击热门
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        #隐式等待
        self.driver.implicitly_wait(3)
    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@id="ember41"]/a').click()
        #直到可被点击
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH, '//*[class=""table-heading]'))
        #元素是否可见. 当我们需要找到元素，并且该元素也可见。
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(By.XPATH, '//*[class=""table-heading]'))
        #当我们不关心元素是否可见，只关心元素是否存在在页面中。
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(By.XPATH, '//*[class=""table-heading]'))
        self.driver.find_element(By.XPATH, "//*[@id='ember195']/a").click()