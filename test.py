import requests
from html.parser import HTMLParser
from urllib.parse import quote


print("沈药校园信息雷达")
print("开始侦察：沈药学工……")
print()

query = 'site:mp.weixin.qq.com/s/ "沈药学工"'
url = "https://www.baidu.com/s?wd=" + quote(query)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 "
        "Mobile/15E148 Safari/604.1"
    )
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    print("百度访问状态码：", response.status_code)
    print("网页长度：", len(response.text), "字符")
    print()

    html = response.text

    class LinkParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.links = []
            self.current_href = None
            self.current_text = []

        def handle_starttag(self, tag, attrs):
            if tag == "a":
                attrs = dict(attrs)
                self.current_href = attrs.get("href")
                self.current_text = []

        def handle_data(self, data):
            if self.current_href is not None:
                self.current_text.append(data)

        def handle_endtag(self, tag):
            if tag == "a" and self.current_href:
                text = "".join(self.current_text).strip()
                self.links.append((text, self.current_href))
                self.current_href = None
                self.current_text = []

    parser = LinkParser()
    parser.feed(html)

    print("搜索结果中的链接数量：", len(parser.links))
    print()
    print("其中包含 mp.weixin.qq.com 的结果：")

    count = 0

    for text, href in parser.links:
        if "mp.weixin.qq.com" in href or "mp.weixin.qq.com" in text:
            count += 1
            print()
            print("【结果", count, "】")
            print("标题：", text[:200])
            print("链接：", href[:500])

    print()
    print("最终找到微信相关链接：", count, "个")
    print()
    print("侦察结束。")

except Exception as e:
    print("发生错误：", type(e).__name__)
    print("错误信息：", e)
