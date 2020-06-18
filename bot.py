import moli
from clock import judge_0
import tuling
import plugins
import threading
from commands import cmds
from cqhttp import CQHttp

# config中 "post_url": "http://127.0.0.1:5701"

bot = CQHttp(api_root='http://127.0.0.1:5700',
             access_token="",
             secret=""
             )

def handle_all_message(context):
    message: str = context['message']
    msg = message.split(maxsplit=1)
    if not msg:
        return ''
    cmd, *args = msg
    arg = ''.join(args)

    if cmd[0] in ['\\', '/', '／']:
        handler = cmds.get(cmd[1:])
    else:
        handler = None

    print('cmd:', cmd)
    print('arg:', arg)
    print('handler:', handler)

    return arg, message, handler

@bot.on_message('private')
def handle_message(context):
    arg, message, handler = handle_all_message(context)

    if handler:
        return handler(context, arg)
    else:
        replies = tuling.get_reply(message)
        if replies:
            if replies[0] == '请求次数超限制!':
                reply = moli.get_reply(message)
                print(reply)
                return {'reply': reply}
            else:
                return {'reply': replies[0]}

@bot.on_message('group')
def handle_message(context):
    arg, message, handler = handle_all_message(context)

    if handler:
        return handler(context, arg)
    elif '[CQ:at,qq=3457292188]' in message:
        replies = tuling.get_reply(message)
        if replies[0] == '请求次数超限制!':
            reply = moli.get_reply(message)
            print(reply)
            return {'reply': reply}
        else:
            return {'reply': replies[0]}

t1 = threading.Thread(target=judge_0)
t1.start()

bot.run(host='127.0.0.1', port=5701, debug=True)
