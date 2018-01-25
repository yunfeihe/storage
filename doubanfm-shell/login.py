import requests
from pprint import pprint
def log(*args):
    print(*args)

def login(login_id, password):
    print(locals())
    login_url = "https://accounts.douban.com/j/popup/login/basic"
    headers = {
                "source":"fm",
                "referer":"https://douban.fm/",
                "name":login_id,
                "password":password,
                "captcha_solution":None,
                "captcha_id":None,
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

    }
    response = requests.post(login_url,headers=headers)
    log(response.text)
    log('code: ', response.status_code)
    log()


def test_index():
    login('18256753032', 'sylove521')

    log('finished')

test_index()
