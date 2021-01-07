from time import sleep
from selenium import webdriver

class TestJs():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")

        '''js方式获取”百度一下“按钮，找到后返回给element'''
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()

        '''滑动到最低端，再点击下一页'''
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)


        '''打印title，打印性能数据'''
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))




    def test_datetime(self):
        #12306首页
        self.driver.get("https://www.12306.cn/index/")
        #定位时间控件,移除元素的readonly属性，使其可以被修改
        time_element = self.driver.execute_script("a = document.getElementById('train_date')","a.removeAttribute('readonly')")
        #给时间控件赋值新value
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-31'")
        sleep(3)



