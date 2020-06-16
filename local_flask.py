from flask import Flask,request
from json import loads

bot_server = Flask(__name__)

@bot_server.route('/api/message',methods=['POST'])
#路径是你在酷Q配置文件里自定义的
def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    QQ = data.get('user_id')
    nickname = data['sender'].get('nickname')
    message = data['message'][0]['data'].get('text')
    print(f"{QQ}:{nickname}:{message}")
    return ''


if __name__ == '__main__':
    bot_server.run(port=5701, debug=True)
    #端口也是你在酷Q配置文件里自定义的