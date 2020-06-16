import requests
from pprint import pprint
from cqhttp import CQHttp

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
