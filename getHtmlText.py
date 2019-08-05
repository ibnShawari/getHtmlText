import requests

def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()      #如果状态不是200 引发httpError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = input("请输入带爬取的网页地址！")
    print(getHtmlText(url))