from flask import Flask,request
from json import loads
import json

bot_server = Flask(__name__)

@bot_server.route('/', methods=['POST'])
def server():
    # data = request.get_data().decode('utf-8')
    # data = loads(data)
    # QQ = data.get('user_id')
    # nickname = data['sender'].get('nickname')
    # message = data['message'][0]['data'].get('text')
    # print(f"{QQ}:{nickname}:{message}")
    user = {
        "username": "L",
        "nickname": "张三"
    }
    return json.dumps(user)


if __name__ == '__main__':
    bot_server.run(host='127.0.0.1', port=9090, debug=True)