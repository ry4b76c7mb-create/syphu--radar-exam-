import requests
import json

print("沈药校园信息雷达")
print("开始测试公众号搜索……")
print()

url = "https://mp.weixin.qq.com/cgi-bin/searchbiz"

params = {
    "action": "search_biz",
    "begin": "0",
    "count": "5",
    "query": "沈药学工",
    "lang": "zh_CN",
    "f": "json"
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Mobile/15E148 Safari/604.1"
    )
}

try:
    print("正在搜索公众号：沈药学工")
    print()

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=20,
        allow_redirects=True
    )

    print("状态码：", response.status_code)
    print("最终地址：", response.url)
    print("返回长度：", len(response.text))
    print()

    print("返回内容前500个字符：")
    print("--------------------------------")
    print(response.text[:500])
    print("--------------------------------")
    print()

    # 尝试解析 JSON
    try:
        data = response.json()

        print("检测到 JSON 返回")
        print("JSON 内容：")
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])

    except Exception:
        print("这次返回的内容不是标准 JSON。")
        print("这通常意味着还需要微信登录会话。")

except Exception as e:
    print("访问失败：", type(e).__name__)
    print("错误信息：", e)

print()
print("公众号搜索测试结束。")
