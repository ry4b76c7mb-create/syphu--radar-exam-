import requests
import re

print("沈药校园信息雷达")
print("开始分析真实微信文章……")
print()

article_url = "https://mp.weixin.qq.com/s/_bKHQm8QKt_u8Q91Rb5pQg"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Mobile/15E148 Safari/604.1"
    )
}

try:
    print("正在访问沈药学工真实文章：")
    print(article_url)
    print()

    response = requests.get(
        article_url,
        headers=headers,
        timeout=20,
        allow_redirects=True
    )

    print("状态码：", response.status_code)
    print("最终地址：", response.url)
    print("网页长度：", len(response.text))
    print()

    html = response.text

    # 尝试寻找公众号内部标识
    patterns = {
        "__biz": r'__biz["\']?\s*[:=]\s*["\']([^"\']+)',
        "biz": r'["\']biz["\']?\s*[:=]\s*["\']([^"\']+)',
        "nickname": r'["\']nickname["\']?\s*[:=]\s*["\']([^"\']+)',
        "appmsgid": r'["\']appmsgid["\']?\s*[:=]\s*["\']?(\d+)',
    }

    print("开始寻找文章中的内部信息……")
    print()

    found = False

    for name, pattern in patterns.items():
        matches = re.findall(pattern, html, re.IGNORECASE)

        if matches:
            found = True
            # 去重
            unique = list(dict.fromkeys(matches))

            print("找到：", name)
            for value in unique[:10]:
                print("  ", value)
            print()

    if not found:
        print("暂时没有找到明显的公众号内部标识。")
        print()

    # 顺便检查几个关键词
    keywords = [
        "沈药学工",
        "SYPHU_XSC",
        "__biz",
        "fakeid",
        "appmsgid"
    ]

    print("关键词检查：")
    for keyword in keywords:
        print(keyword, "→", keyword in html)

    print()
    print("真实文章分析结束。")

except Exception as e:
    print("访问失败：", type(e).__name__)
    print("错误信息：", e)
