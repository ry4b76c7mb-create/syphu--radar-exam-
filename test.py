import requests

print("沈药校园信息雷达")
print("开始测试微信登录态……")
print()


# 这里暂时先放测试位置
cookie = "你的微信Cookie"


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 Chrome/120 Safari/537.36"
    ),
    "Cookie": cookie
}


url = "https://mp.weixin.qq.com/cgi-bin/searchbiz"


params = {
    "action": "search_biz",
    "begin": "0",
    "count": "5",
    "query": "沈药学工",
    "lang": "zh_CN",
    "f": "json"
}


try:

    print("正在请求微信公众号搜索接口……")
    print()

    r = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )


    print("状态码：", r.status_code)

    print()

    print("返回内容：")
    print(r.text[:1000])


except Exception as e:

    print("错误：", e)
