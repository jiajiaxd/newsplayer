import requests
import json
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = requests.get(
        "https://api.cntv.cn/lanmu/columnSearch?&fl=&fc=%E6%96%B0%E9%97%BB&cid=&p=1&n=20&serviceId=tvcctv&t=jsonp&cb"
        "=Callback")
    res = json.loads(response.text.removeprefix('Callback(').removesuffix(');'))
    res = res.get('response').get("docs")[14].get('lastVIDE')
    print("获取到", res.get('videoTitle'), res.get('videoUrl'))
    print("调出浏览器...")
    os.system("start " + res.get('videoUrl'))
    os.system('pause')
