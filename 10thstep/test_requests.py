import requests

def test_demo():
    url ="http://httpbin.ceshiren.com/cookies"
    header = {
        'User-Agent': 'hogwarts'
              }
    cookie_data={
        "hogwarts": "school",
        "teacher":"AD"
    }
    r=requests.get(url = url,headers = header,cookies=cookie_data)
    print(r.request.headers)