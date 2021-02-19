import requests
from bs4 import BeautifulSoup
import ffmpy3

# 1.获取网页的源代码
base_url = "https://www.okzyw.net/?m=vod-detail-id-69001.html"
res = requests.get(base_url).text

# 2.解析m3u8地址
# 实例化对象
selector = BeautifulSoup(res, 'html.parser')  # 也可以写成 lxml 不过此处写lxml报错
# 查找所有符合条件的元素
result_list = selector.find_all('input')
page = 1
for item in result_list:
    # print(result_list)
    if 'm3u8' in item.get('value'):
        # print(item.get('value')) # 筛选出符合的url
        ffmpy3.FFmpeg(inputs={item.get('value'): None}, outputs={'第{}集.mp4'.format(page): None}).run()
        print('第{}集 下载完成！！！'.format(page))
        page += 1

