import re
import time
import requests

def get_reply(message):
    payload = {'question': message,
               'limit': 6,
               'Api_Key': '',
               'Api_Secret': ''
               }

    url = 'http://i.itpk.cn/api.php'
    r = requests.get(url, params=payload)

    if re.findall(r".?笑话", message):
        text = r.content.decode('unicode-escape').split('"')
        title = text[3]
        content = text[-2]

        # title = re.findall(r'"title":"(.*?)"', text)
        # content = re.findall(r'"content":"(.*?)"', text)
        print(text)
        if title and content:
            return f"《{title}》\n{content}"
        else:
            return "人家刚才打盹了呢,请再说一遍吧 >_<"
    else:
        return r.text
