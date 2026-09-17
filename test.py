import urllib.request

print("沈药校园信息雷达")
print("开始测试云端网络……")

urls = [
    "https://www.baidu.com",
    "https://mp.weixin.qq.com",
    "https://mp.weixin.qq.com/s/_bKHQm8QKt_u8Q91Rb5pQg"
]

for url in urls:
    print("\n正在访问：", url)

    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            print("状态码：", response.status)
            print("访问成功！")

    except Exception as e:
        print("访问失败：", type(e).__name__)
        print("错误信息：", e)

print("\n网络测试结束。")
