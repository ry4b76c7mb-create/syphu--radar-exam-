import requests
from urllib.parse import quote


print("沈药校园信息雷达")
print("开始测试微信公众号搜索接口……")
print()


keyword = "沈药学工"

url = (
    "https://mp.weixin.qq.com/cgi-bin/searchbiz"
    "?action=search_biz"
    "&begin=0"
    "&count=5"
    "&query="
    + quote(keyword)
    + "&lang=zh_CN"
)


headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"
        " AppleWebKit/605.1.15"
        " Mobile/15E148 Safari/604.1"
    ),
    "Referer": "https://mp.weixin.qq.com/"
}


try:

    print("请求地址:")
    print(url)
    print()


    r = requests.get(
        url,
        headers=headers,
        timeout=20
    )


    print("状态码:", r.status_code)
    print()


    # 微信返回通常是json
    print("返回前500字符:")
    print("----------------")

    print(r.text[:500])


    print("----------------")


except Exception as e:
    print("错误:")
    print(e)
