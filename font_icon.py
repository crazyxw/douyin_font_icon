# -*- coding: utf-8 -*-

import requests
from lxml import etree

font_map = {
    "58882": "1",
    "58883": "0",
    "58884": "3",
    "58885": "2",
    "58886": "4",
    "58887": "5",
    "58888": "6",
    "58889": "9",
    "58890": "7",
    "58891": "8",
    "58892": "4",
    "58893": "0",
    "58894": "1",
    "58895": "5",
    "58896": "2",
    "58897": "3",
    "58898": "6",
    "58899": "7",
    "58900": "8",
    "58901": "9",
    "58902": "0",
    "58903": "2",
    "58904": "1",
    "58905": "4",
    "58906": "3",
    "58907": "5",
    "58908": "7",
    "58909": "8",
    "58910": "9",
    "58911": "6",

}


def font_convert(temp: list) -> str:
    fonts = []
    for i in temp:
        t = i.strip()
        if not t:
            continue
        elif t in [".", "w"]:
            fonts.append(t)
        else:
            fonts.append(font_map[str(ord(t))])
    return "".join(fonts)


url = "https://www.douyin.com/share/user/56874100517"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

response = requests.get(url, headers=headers)

html = etree.HTML(response.text)

focus_num = html.xpath("//span[@class='focus block']/span[@class='num']//text()")

print("关注数: ", font_convert(focus_num))

follower = html.xpath("//span[@class='follower block']/span[@class='num']//text()")
print("粉丝数: ", font_convert(follower))

like = html.xpath("//span[@class='liked-num block']/span[@class='num']//text()")
print("点赞数: ", font_convert(like))
