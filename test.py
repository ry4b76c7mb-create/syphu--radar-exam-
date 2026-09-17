import requests

print("沈药校园信息雷达")
print("开始测试微信服务器连接……")
print()

urls = [
    "https://mp.weixin.qq.com",
    "https://mp.weixin.qq.com/cgi-bin/searchbiz",
    "https://mp.weixin.qq.com/cgi-bin/appmsg",
]

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Mobile/15E148 Safari/604.1"
    )
}

for url in urls:
    try:
        print("正在访问：", url)

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
            allow_redirects=True
        )

        print("状态码：", response.status_code)
        print("最终地址：", response.url)
        print("网页长度：", len(response.text))
        print()

    except Exception as e:
        print("访问失败：", type(e).__name__)
        print("错误信息：", e)
        print()

print("微信服务器探针结束。")
