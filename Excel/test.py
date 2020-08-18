import requests
from bs4 import BeautifulSoup
import json
import time
import xlwt

# url = "https://www.nosetime.com/search.php?op=ajax&type=all&word="
url = "https://www.nosetime.com/search.php?op=ajax&type=3&start=10&page=2&perpage=10&word="
# url = "https://www.nosetime.com/search.php?op=ajax&type=3&start=10&page=3&perpage=10&word="
# kw = {
#     "op": "ajax",
#     "type": "3",
#     "word": "迪奥",
#     # "start": "10",
#     # "page": "3",
#     # "perpage": "10"
# }

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "Hm_lvt_6a84a39e64fe0723de5722134963fcfe=1597672709,1597723093; Hm_lpvt_6a84a39e64fe0723de5722134963fcfe=1597752620",
    # "referer": "https://www.nosetime.com/search.php?x=0&y=0&word=%E4%BF%A1%E4%BB%B0%E6%8B%BF%E7%A0%B4%E4%BB%91%E4%B9%8B%E6%B0%B4",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59"
}

# rsp = requests.get(url,params=kw, headers=headers).text
#
# #print(rsp)
# print("================================")
# items = json.loads(rsp)
# #print("item:", items["item"])
# i = 0
# for item in items["item"]["data"]:
#     i += 1
#     print(i)
#     print("香水名:",item["title"])
#     print("前调:",item["itopnotes"])
#     print("中调:",item["imiddlenotes"])
#     print("后调:",item["ibasenotes"])

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('perfumeList')
# 在excel中添加香水品牌
worksheet.write(0, 0, label='香水品牌')
worksheet.write(0, 1, label='前调')
worksheet.write(0, 2, label='中调')
worksheet.write(0, 3, label='后调')

# 写入excel
# 参数对应 行, 列, 值
# worksheet.write(0,0, label = 'this is test')
perfumeName = "范思哲"

k = 0
try:
    for i in range(1, 11):
        url = "https://www.nosetime.com/search.php?op=ajax&type=3&start=10&page={page}&perpage=10&word=".format(page=i)
        # print(url)
        kw = {
            "op": "ajax",
            "type": "3",
            "word": "{}".format(perfumeName),
            "start": "10",
            "page": "{}".format(i),
            "perpage": "10"
        }
        # print(kw)

        rsp = requests.get(url, params=kw, headers=headers).text

        # print(rsp)
        print("================================")
        items = json.loads(rsp)
        # print("item:", items["item"])
        for item in items["item"]["data"]:
            k += 1
            print(k)
            print("香水名:", item["title"])
            worksheet.write(k, 0, label='{}'.format(item["title"]))
            print("前调:", item["itopnotes"])
            worksheet.write(k, 1, label='{}'.format(item["itopnotes"]))
            print("中调:", item["imiddlenotes"])
            worksheet.write(k, 2, label='{}'.format(item["imiddlenotes"]))
            print("后调:", item["ibasenotes"])
            worksheet.write(k, 3, label='{}'.format(item["ibasenotes"]))

        time.sleep(5)
finally:
    workbook.save('D:\\perfume\\{}.xls'.format(perfumeName))
