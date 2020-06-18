import requests

def reply_msg(type_, message, user_id=296491216, group_id=660322651):
    data = {
        "access_token": "L",
        "message": message,
        "auto_escape": False
    }
    if not message:
        return ''
    if type_ == 'private' and user_id:
        data["user_id"] = user_id
    elif type_ == 'group' and group_id:
        data["group_id"] = group_id
    else:
        return ''
    api_url = f'http://127.0.0.1:5700/send_{type_}_msg'
    r = requests.get(api_url, params=data)

    print(r.text, r)