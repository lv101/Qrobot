'''
向指定id用户/群组发送消息
'''
import requests

def reply_msg(type_, message, user_id=296491216, group_id=660322651):
    data = {
        "access_token": "L",  # 你的配置文件中access_token, 没有可不填
        "message": message,
        "auto_escape": False
    }
    if not message:
        return ''
    if type_ == 'private' and user_id:
        data["user_id"] = user_id
    elif type_ == 'group' and group_id:
        data["group_id"] = group_id
        data["message"] = f"[CQ:at,qq=user_id']\n" + data["message"]
    else:
        return ''
    api_url = f'http://127.0.0.1:5700/send_{type_}_msg'
    r = requests.get(api_url, params=data)

    print(r.text, r)

def check_id(context):
    context["user_id"] = context.get("user_id", None)
    context["group_id"] = context.get('group_id', None)