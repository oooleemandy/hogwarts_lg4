from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCSSS():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_fnd(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("Hogwarts")
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()