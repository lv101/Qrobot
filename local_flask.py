from json import loads

from flask import Flask, request

bot_server = Flask(__name__)

@bot_server.route('/', methods=['POST'])
def server():
    # data = {}
    data = request.get_data().decode('utf-8')
    data = loads(data)
    QQ = data.get('user_id')
    nickname = data['sender'].get('nickname')
    message = data['message']
    print(f"{QQ}:{nickname}:{message}")
    return ''

if __name__ == '__main__':
    bot_server.run(host='127.0.0.1', port=5701, debug=True)
