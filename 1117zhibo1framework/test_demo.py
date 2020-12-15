'''
web自动化搜索
'''
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_data(path):
    with open(path, encoding='utf-8') as f:w
    return yaml.load(f)

def test_load_data()



class TestDemo:
    #参数化
    @pytest.mark.parametrize("keyword",load_data("test_data.yaml"))
    def test_search(self,keyword):
        driver = webdriver.Chrome()
        driver.get("https://ceshiren.com")
        driver.find_element(By.ID, 'search-button').click()
        driver.find_element(By.ID, 'search-term').send_keys(keyword)


    if 'get' in step:
        url = step.get('get')
        driver.get(url)

    if 'find_element' in step:
        by = step.get(find)











