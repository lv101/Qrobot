import moli
import tuling
import plugins
from commands import cmds


from cqhttp import CQHttp


bot = CQHttp(api_root='http://127.0.0.1:5700',
             access_token="L",
             secret="2333"
             )

@bot.on_message('private')
def handle_message(context):
    message: str = context['message']
    msg = message.split(maxsplit=1)
    if not msg:
        return ''
    cmd, *args = msg
    arg = ''.join(args)
    handler = cmds.get(cmd)
    print('cmd:', cmd)
    print('arg:', arg)
    print('handler:', handler)

    if cmd[0] == '\\':
        handler = cmds.get(cmd[1:])
    else:
        handler = None

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
    message: str = context['message']
    msg = message.split(maxsplit=1)
    if not msg:
        return ''
    cmd, *args = msg
    arg = ''.join(args)
    if cmd[0] == '\\':
        handler = cmds.get(cmd[1:])
    else:
        handler = None
    print('cmd:', cmd)
    print('arg:', arg)
    print('handler:', handler)
    print(context)

    if handler:
        return handler(context, arg)
    elif '[CQ:at,qq=3457292188]' in message:
        if context['user_id'] == 296491216:
            return {'reply': "您说的对！"}
        replies = tuling.get_reply(message)
        if replies[0] == '请求次数超限制!':
            reply = moli.get_reply(message)
            print(reply)
            return {'reply': reply}
        else:
            return {'reply': replies[0]}

bot.run(host='127.0.0.1', port=5701, debug=True)