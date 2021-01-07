import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        '''复用浏览器，创建option。option制定浏览器启动debug地址。传进option'''
        option = Options()
        option.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def test_add_contact(self):
        #cookies = self.driver.get_cookies()
        cookies = [{'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False,
                    'value': 'o0137787592'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1641444557.818233, 'httpOnly': False,
                    'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
                   {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False,
                    'value': '@2J2LvbQDD'},
                   {'domain': '.qq.com', 'expiry': 2147483430.511013, 'httpOnly': False, 'name': 'RK', 'path': '/',
                    'secure': False, 'value': 'JMJcSTgSG7'},
                   {'domain': '.qq.com', 'expiry': 2147483430.511117, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                    'secure': False, 'value': '0c1a882cad52a4cbc5005d9fc4854a9ca4021eb49f19f142d1c2ae1dce46acc0'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1641559039, 'httpOnly': False,
                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                    'value': '1609908568,1610023039'},
                   {'domain': '.qq.com', 'expiry': 1673097367, 'httpOnly': False, 'name': '_ga', 'path': '/',
                    'secure': False, 'value': 'GA1.2.1128381225.1609908570'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1612617440.930347, 'httpOnly': False,
                    'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
                    'secure': False, 'value': 'direct'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                    'secure': False, 'value': '03184142'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                    'secure': False, 'value': '1'},
                   {'domain': 'work.weixin.qq.com', 'expiry': 1610028127.526147, 'httpOnly': True, 'name': 'ww_rtkey',
                    'path': '/', 'secure': False, 'value': '3kc9kf'},
                   {'domain': '.qq.com', 'expiry': 1610111767, 'httpOnly': False, 'name': '_gid', 'path': '/',
                    'secure': False, 'value': 'GA1.2.188972918.1609996592'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                    'secure': False, 'value': '1970324943175019'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                    'secure': False, 'value': '1688854068709900'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                    'secure': False, 'value': '1688854068709900'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
                                                                    'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
                                                                    'path': '/', 'secure': False,
                                                                    'value': '1610023039'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                    'secure': False, 'value': 'a9866635'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                    'secure': False, 'value': 'HGCZDgTSb3atjZZild4lXkWMDU5axgCRbaNpnyGp0ooQVCaO9vpYSREdAcEFBt4C'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/',
                    'secure': False,
                    'value': 'h79gUTyxE73XyGRdmnZlXSZGnpv7sceWYz_7-_proe7OZJZki3yhGvHSscbwzbGBohqp0PDpxcfScFPDYPHj8K9Y7muKY9zi8Xnwo3cBGmsi0pO0gQ0IRCkONVp_nwfkGmdQ9nLqqIkmBr3wCPFg8K9L1R8zJJEMRAE8NJmpqrnJdthDwxAwCh1j5tnFRSJlKc9-579wuzIqe6gFSZCtq1vT9v8wIJD2RlPhtftEzUwDOiuYAjiyhk8G-8OTVlfUZmL4JUiVuwqK3Y4_cDf7zA'}]
        #print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")


        '''以上cookie列表中有多个字典，for循环遍历列表，让每一个字典都放进'''
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        #点击添加成员
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        #输入姓名
        self.driver.find_element_by_id("username").send_keys("DD")
        #输入账号
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("dd")
        #输入手机号
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13044444444")
        #点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        assert "保存成功！"
