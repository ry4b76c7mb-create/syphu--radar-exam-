import requests
from urllib.parse import quote

print("沈药校园信息雷达")
print("开始检查百度返回内容……")
print()

query = 'site:mp.weixin.qq.com/s/ "沈药学工"'
url = "https://www.baidu.com/s?wd=" + quote(query)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Mobile/15E148 Safari/604.1"
    )
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    html = response.text

    print("百度状态码：", response.status_code)
    print("网页长度：", len(html), "字符")
    print()

    checks = [
        "沈药学工",
        "mp.weixin.qq.com",
        "百度安全验证",
        "验证码",
        "安全验证",
        "访问异常",
        "请完成验证",
    ]

    print("关键词检查：")

    for word in checks:
        print(word, "→", "找到" if word in html else "没有")

    print()
    print("百度返回内容前 1000 个字符：")
    print("--------------------------------")
    print(html[:1000])
    print("--------------------------------")
    print()
    print("检查结束。")

except Exception as e:
    print("发生错误：", type(e).__name__)
    print("错误信息：", e)
