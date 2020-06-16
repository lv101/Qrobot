'''
指定命令执行的功能
'''
import requests
from math import *
from commands import command

@command('echo')
def echo(context, arg):
    return {'reply': arg}

@command('chp')
def chp(context, arg):
    r = requests.get('https://chp.shadiao.app/api.php')
    return {'reply': r.text}

@command('jisuan')
def jisuan(context, arg):
    try:
        expression = arg.strip()
        print(expression)
        return {'reply': f'{expression}='+str(eval(expression))}
    except:
        return {'reply': '这个算术题好难,人家算不出来呢 >_<'}

@command('help')
def help(context, arg):
    reply = "\n        帮助菜单\n" \
            "\t\\echo -> 复读机\n" \
            "\t\\chp -> 彩虹屁\n" \
            "\t\\jisuan -> 计算器\n"
    return {'reply': reply}