import requests
from hamcrest import *
from jsonpath import jsonpath

class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.ceshiren.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200


    def test_query(self):
        #载体
        payload = {
            "level":1,
            "name":"leemandy"
        }
        r = requests.get('http://httpbin.ceshiren.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200


    def test_post_form(self):
        # 载体
        payload = {
            "level": 1,
            "name": "leemandy"
        }
        r = requests.post('http://httpbin.ceshiren.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('http://httpbin.ceshiren.com/get',headers={"h":"header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']["H"] == "header demo"


    def test_post_json(self):

        r = requests.post('http://httpbin.ceshiren.com/post')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        ##assert r.json()['category_list']['categories'][0]['name'] =='开源项目'
        print(jsonpath(r.json(),'$..name'))
        assert jsonpath(r.json(),'$..name')[0] == '开源项目'

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('开源项目'))

