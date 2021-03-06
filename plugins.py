'''
指定命令执行的功能
'''
import json
import random
import re
import time
import requests
import threading
from math import *
from bdy import main
from commands import command
from replys import reply_msg, check_id

@command('echo')
def echo(context, arg):
    return {'reply': arg}

@command('chp')
def chp(context, arg):
    r = requests.get('https://chp.shadiao.app/api.php')
    return {'reply': r.text, 'at_sender': False}

@command('jisuan')
def jisuan(context, arg):
    try:
        expression = arg.strip()
        print(expression)
        return {'reply': f'{expression}='+str(eval(expression))}
    except:
        return {'reply': '这个算术题好难,人家算不出来呢 >_<'}

@command('fanyi')
def fanyi(context, arg):
    if not arg:
        return {'reply': '人家没有看到要翻译的内容呢,再试一次吧 >-<'}

    paylod = {'doctype': 'json',
              'type': 'AUTO',
              'i': args}
    url = 'http://fanyi.youdao.com/translate'
    data = requests.get(url, params=paylod).json()

    type_ = data["type"]
    error = data["errorCode"]
    results = data["translateResult"]
    if type_ == "UNSUPPORTED":
        return {'reply': "这个词好深奥,人家不会呢,换个词试试吧 >_<"}
    else:
        trans = []
        for result in results:
            text = result[0]["tgt"]
            if text:
                trans.append(text)
        result_info = '\n'.join(trans)
        return {'reply': result_info}


@command('tianqi')
def tianqi(context, arg):
    with open('city.json', 'r', encoding='unicode-escape') as f:
        citys = json.loads(f.read())
    city = None
    for city_ in citys:
        if re.findall(city_['cityZh'], arg):
            city = city_['cityZh']
            print(city)
            break
    check_id(context)
    if not city:
        time.sleep(3)
        reply_msg(context['message_type'], "啊哦,没有查到该地的信息,换个城市试试吧 >_<",
                  group_id=context['group_id'], user_id=context['user_id'])
        return ''

    paylod = {
        'version': 'v6',
        'appid': ,
        'appsecret': '',
        'city': city
    }

    url = 'https://tianqiapi.com/api'
    r = requests.get(url, params=paylod).content.decode('unicode-escape').replace('<\/em><em>', '')
    data = json.loads(r)

    reply_msg(context['message_type'], f"{data['country']}{data['city']}\n更新时间：{data['update_time']}\n"
              f"天气情况：{data['wea']}\n实时温度：{data['tem']}\n气压：{data['pressure']}hPa\n"
              f"空气质量：{data['air']}\n"f"空气质量等级：{data['air_level']}\n{data['air_tips']}",
              group_id=context['group_id'], user_id=context['user_id'])

@command('tianqi7')
def tianqi7(context, arg):
    with open('city.json', 'r', encoding='unicode-escape') as f:
        datas = json.loads(f.read())
    city = None
    for data in datas:
        if re.findall(data['cityZh'], arg):
            city = data['cityZh']
            print(city)
    check_id(context)

    if not city:
        time.sleep(3)
        reply_msg(context['message_type'], "啊哦,没有查到该地的信息,换个城市试试吧 >_<",
                  group_id=context['group_id'], user_id=context['user_id'])
        return ''

    paylod = {
              'version': 'v1',
              'appid': ,
              'appsecret': '',
              'city': city
                  }

    url = 'https://tianqiapi.com/api'
    r = requests.get(url, params=paylod).content.decode('unicode-escape').replace('<\/em><em>', '')

    text = json.loads(r)

    for data in text['data']:
        desc_list = []
        for x in data['index']:
            desc_list.append(x['desc'])
        desc = desc_list[random.randint(0, len(desc_list) - 1)]
        check_id(context)
        reply_msg(context['message_type'], f"{text['country']}{text['city']}\n"f"更新时间：{text['update_time']}\n"
                  f"{data['day']}\n"f"天气情况：{data['wea']}\n平均温度：{data['tem']}\n{desc}",
                  group_id=context['group_id'], user_id=context['user_id'])
        time.sleep(1)

@command('ask')
def ask(context, arg):
    if not arg:
        print('请输入你想要预测的问题,人家没有看到呢 *_*')
    if context['user_id'] == 296491216:
        reply = 'Yes'
    else:
        x = random.randint(0, 1)
        if x:
            reply = 'Yes'
        else:
            reply = 'No'
    return {'reply': reply}

@command('help')
def help(context, arg):
    reply = "        帮助菜单\n" \
            "\t/echo -> 复读机\n" \
            "\t/ask -> 推衍\n" \
            "\t/chp -> 彩虹屁\n" \
            "\t/jisuan -> 计算器\n" \
            "\t/fanyi -> 有道翻译\n" \
            "\t/tianqi -> 天气预报\n" \
            "\t/tianqi7 -> 未来7天天气"

    check_id(context)
    reply_msg(context['message_type'], reply, group_id=context['group_id'], user_id=context['user_id'])
    reply_msg(context['message_type'], "我的源码放在https://github.com/lv101/Qrobot\n尽情探索吧~", group_id=context['group_id'], user_id=context['user_id'])
