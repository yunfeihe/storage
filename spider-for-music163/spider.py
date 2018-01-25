import requests
from bs4 import BeautifulSoup
from pprint import pprint


def get_response_from_url(url):
    headers = {
        "Accept":"""text/html,application/xhtml+xml,application/xml
            ;q=0.9,image/webp,image/apng,*/*;q=0.8""",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Host":"music.163.com",
        "Referer":"http://music.163.com/",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

         }
    response = requests.post(url, headers=headers)
    return response

test = get_response_from_url('http://music.163.com/#/user/home?id=1512211')
pprint(test.text)
