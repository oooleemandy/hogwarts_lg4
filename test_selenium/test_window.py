from time import sleep

from test_pytest.base import Base


class TestWindow(Base):

    '''
    百度首页-点击登陆-点击立刻注册
    '''
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        #打印出当前窗口
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        #跳出新的窗口需要在新的窗口里找
        print(self.driver.current_window_handle)
        #打印所有窗口
        print(self.driver.window_handles)
        #定义当前的所有窗口
        windows=self.driver.window_handles
        #此时形成一个窗口列表，去倒数第一个窗口里找
        self.driver.switch_to_window(windows[-1])
        #输入用户名密码
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("oooleemandy")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("15566274527")

        #再切换回登陆的窗口,第一个窗口
        self.driver.switch_to_window(windows[0])
        #点击用户名登陆
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        #输入用户名密码
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("oooleemandy")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("limandi940905")
        #点击登陆
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()


        sleep(3)


