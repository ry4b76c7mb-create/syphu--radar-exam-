import urllib.request
import urllib.parse
import re

print("沈药校园信息雷达")
print("开始侦察：沈药学工……")

query = 'site:mp.weixin.qq.com/s "沈药学工"'
url = "https://www.baidu.com/s?" + urllib.parse.urlencode({
    "wd": query
})

print("\n正在访问搜索引擎……")
print(url)

try:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        html = response.read().decode("utf-8", errors="ignore")

    print("搜索访问成功！")
    print("网页长度：", len(html), "字节")

    # 从搜索结果中寻找微信文章链接
    links = re.findall(
        r'https?://mp\.weixin\.qq\.com/s/[A-Za-z0-9_-]+',
        html
    )

    # 去重，保持原来的顺序
    unique_links = []
    for link in links:
        if link not in unique_links:
            unique_links.append(link)

    print("\n找到微信文章链接：", len(unique_links), "个")

    for i, link in enumerate(unique_links[:10], 1):
        print(f"{i}. {link}")

except Exception as e:
    print("\n搜索失败！")
    print(type(e).__name__)
    print(e)

print("\n侦察结束。")
