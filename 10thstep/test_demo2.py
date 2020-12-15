import requests
from requests.auth import HTTPBasicAuth


class Api:
    data={
        "method":"get",
        "url":"url",
        "headers":None,
    }


    #data 是一个请求信息
    def send(self,data:dict):
        requests.request(method=data["method"] , url =data["url"] ,headers = data["headers"] )