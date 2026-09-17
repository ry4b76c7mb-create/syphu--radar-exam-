import requests
import re

print("沈药校园信息雷达")
print("开始提取公众号身份信息……")
print()

url = "https://mp.weixin.qq.com/s/_bKHQm8QKt_u8Q91Rb5pQg"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

html = r.text

print("网页长度：", len(html))
print()

keys = [
    "bizuin",
    "__biz",
    "fakeid",
    "nickname",
    "沈药学工",
    "SYPHU_XSC"
]

for key in keys:
    print("\n========", key, "========")

    positions = [m.start() for m in re.finditer(key, html)]

    print("出现次数：", len(positions))

    for p in positions[:3]:
        start = max(0, p-150)
        end = min(len(html), p+300)

        print(html[start:end])
        print("----------------")
