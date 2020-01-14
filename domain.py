import requests
import time

domain = "bpg.me"
ftqqskey = "SCU76694T262427b2a6a252669369cb134a12f7b75e15b745eebc5"


def if_domain_registed(domain: str) -> bool:
    url = f'http://xx8.org/index.php?domain={domain}'
    resp = requests.get(url=url)

    return(not "No match for" in resp.text)


def send_to_ftqq(title: str, text: str = '') -> bool:
    url = f'https://sc.ftqq.com/{ftqqskey}.send'
    data = {
        'text': str(title),
        'desp': str(text)
    }
    resp = requests.post(url=url, data=data)

    try:
        jsondict = resp.json()
        errno = int(jsondict.get('errno', -1))
        if errno == 0:
            return(True)
        else:
            return(False)
    except ValueError as e:
        print(f'FTQQ推送出错[{e}]')
        return(False)


while True:
    try:
        if not if_domain_registed(domain):
            current_time = time.asctime(time.localtime(time.time()))
            send_to_ftqq('域名可注册', f'域名：{domain}\n时间：{current_time}')
    finally:
        time.sleep(30)