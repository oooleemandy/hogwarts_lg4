import allure


@allure.link("https://www.baidu.com")
def test_with_link():
    print(("这是一条加了链接的测试"))
    pass
