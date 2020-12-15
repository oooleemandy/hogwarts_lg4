# Generated by Selenium IDE
import shelve

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestTestclick():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.implicitly_wait(5)

  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testclick(self):
    self.driver.get("https://ceshiren.com/")
    self.driver.find_element(By.LINK_TEXT, "所有分类").click()
    element=self.driver.find_element(By.LINK_TEXT, "所有分类")
    result= element.get_attribute("class")
    assert 'active' ==result
    # self.driver.find_element(By.CSS_SELECTOR, "#ember129 .category-name").click()
    # self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.close()

  def test_wx(self):
      self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
      sleep(10)


  def test_case2(self):
    # shelve python 自带的对象持久化存储
    db = shelve.open('cookies')
    db['cookies'] = []