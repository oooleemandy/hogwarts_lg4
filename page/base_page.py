'''
放一些公共的方法。页面的一些都会用到的操作
'''
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    #访问的url
    _base_url=""

    #初始化
    #构造方法 会自动调用
    def __init__(self,driver:WebDriver=None):
        #如果不传driver，每个页面都要初始化一次driver。下面复用driver，而不是每次调用。当testcase很多时不用每次都新初始化driver
        if driver is None:
            self._driver=webdriver.Chrome()
        else:
            self._driver=driver

        #封装url 加一个判断,如果url不为空，就进行一个访问
        if self._base_url !="":
            self._driver.get(self._base_url)


    #封装一个find方法,传一个by一个定位
    def find(self,by,locator):
        return self._driver.find_element(by,locator)