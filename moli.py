'''
茉莉机器人模块,解决图灵机器人对话次数上限问题
'''
import re
import requests

def get_reply(message):
    payload = {'question': message,
               'limit': 6,
               'Api_Key': '40103ccd595f5151a664c8db2fc54aa2',
               'Api_Secret': 'zg9tykwdaj5y'
               }

    url = 'http://i.itpk.cn/api.php'
    r = requests.get(url, params=payload)

    if re.findall(r"笑话", message):
        text = r.content.decode('unicode-escape')
        title = re.findall(r'"title":"(.*?)"', text, re.S)[0]
        content = re.findall(r'"content":"(.*?)"', text, re.S)[0]
        if title and content:
            return f"《{title}》\n{content}"
        else:
            return "人家刚才打盹了呢,再说一次吧 >_<"
    else:
        return r.text
