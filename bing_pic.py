import requests
from lxml import etree
from replys import reply_msg
from fake_useragent import UserAgent

url = "https://cn.bing.com"
headers = {"User-Agent": UserAgent().random}
def bing_t():
    try:
        print("正在抓取图片中,请稍候...")
        r_text = requests.get(url, headers=headers).text
        tags = etree.HTML(r_text)
        url_pic = tags.xpath('//link[@id="bgLink"]/@href')[0]
        img_url = url + url_pic
        img_info = tags.xpath('//a[@id="sh_cp"]/@title')[0]
        message = f"#每日一图#\n{img_info}\n{img_url}"
        if message:
            print("爬取成功")
            reply_msg('group', message)
            return 1
        else:
            return 0
    except:
        return 0