import requests
from pprint import pprint

from cqhttp import CQHttp
#
# data_private = {
#     'user_id': 296491216,
#     'message': 'hello',
#     'auto_escape': False
# }
#
# data_group = {
#     'group_id': 660322651,
#     'message': 'hello'
# }
# data_delete = {
#     'message_id': 104
# }
# data_send_like = {
#     'user_id': 296491216,
#     'times': 3
# }
# key_word = 'send_private_msg'
# # key_word = '/get_friend_list'
# api_url = f'http://127.0.0.1:5700/send_private_msg'
# r = requests.post(api_url, data_private)
# print(r.text)
# import tuling  # 导入图灵模块
# import plugins  # 导入所有命令，虽然后面没有直接用到，但不能删掉
# from command import command_handlers
#
# bot = CQHttp(api_root='http://127.0.0.1:5700')
#
#
# # 注册私聊消息处理函数
# @bot.on_message('private')
# def handle_msg(ctx):
#     pprint(ctx)
#     msg: str = ctx['message']
#     sp = msg.split(maxsplit=1)
#     if not sp:
#         return
#
#     cmd, *remained = sp
#     arg = ''.join(remained)
#     print('cmd:', cmd)
#     print('arg:', arg)
#
#     handler = command_handlers.get(cmd)
#     print('handler:', handler)
#
#     if handler:
#         return handler(bot, ctx, arg)
#     else:
#         replies = tuling.get_reply(msg)
#         if replies:
#             return {'reply': replies[0]}
#
#
# bot.run('127.0.0.1', 8080)

bot = CQHttp(api_root='http://127.0.0.1:5700',
             access_token="L",
             secret="2333"
             )
@bot.on_message('private')
def haddle_message(context):
    user_id = context['sender']['user_id']
    nickname = context['sender']['nickname']
    message = context['message']
    if message.startswith('echo '):
        bot.send(context, message[5:])
    elif message == 'chp':
        r = requests.get('https://chp.shadiao.app/api.php')
        bot.send(context, r.text)
    print(message)

bot.run(host='127.0.0.1', port=5701, debug=True)
