#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 21:31
# @Author  : Roohom
# @Site    : 
# @File    : zhilian_recruit.py
# @Software: PyCharm

"""
爬取智联招聘职位信息
本版本爬取的是合肥地区的职位信息

智联招聘加了反爬 所以本案例没有成功

初步分析是post方式请求了baseurl
返回了json数据
可是怎么获取那个json我还不懂
0: {number: "CCL1218257360J00612851401", jobName: "Python开发工程师",…}
1: {number: "CC839227670J00462415708", jobName: "python爬虫工程师",…}
2: {number: "CC214425823J00219834707", jobName: "python软件工程师",…}
3: {number: "CC217000521J90271561000", jobName: "IT培训讲师（Python）",…}
4: {number: "CC306222811J00455878902", jobName: "python研发工程师",…}
5: {number: "CC415698432J00333293404", jobName: "亚马逊Python开发工程师",…}
6: {number: "CC120564550J00080758808", jobName: "银行SAS/R/PYTHON数据分析挖掘建模岗",…}
7: {number: "CC318512289J00603253105", jobName: "Python/javaScript程序员",…}
8: {number: "CCL1203372320J00362190102", jobName: "Java/C++/Python/Operating system讲师",…}
9: {number: "CC593593127J00629300301", jobName: "全栈开发工程师(Python/Java、Vue)",…}
10: {number: "CCL1201589080J00641960105", jobName: "数据处理&数据挖掘(SPSS/Python 初级)",…}
11: {number: "CC397704085J00632133901", jobName: "大数据开发（驻场合肥）",…}
12: {number: "CC198447026J00539021907", jobName: "数据库开发工程师",…}
13: {number: "CC481300680J00391813205", jobName: "电力软件工程师（应用方向）",…}
14: {number: "CC593593127J00629307401", jobName: "Python工程师",…}
15: {number: "CC342689820J90250002000", jobName: "Java web软件工程师",…}
16: {number: "CC198834412J00395336202", jobName: "程序开发员",…}
17: {number: "CC671623323J00641668305", jobName: "爬虫工程师",…}
18: {number: "CC232405817J00171778009", jobName: "数据分析工程师（CSZN18-zyl）",…}
19: {number: "CC192745913J00156898409", jobName: "C/C++ 工程师(合肥)",…}
20: {number: "CC845377160J00639177005", jobName: "数据处理工程师",…}
21: {number: "CC120747254J00137188714", jobName: "java开发工程师",…}
22: {number: "CC566973936J00481238202", jobName: "应用软件开发工程师",…}
23: {number: "CC806591020J00560808807", jobName: "赴日软件工程师",…}
24: {number: "CC579165785J00377745403", jobName: "对日软件开发",…}
25: {number: "CC553730724J00621853101", jobName: "大数据开发工程师",…}
26: {number: "CC387097722J00206603805", jobName: "大数据工程师",…}
27: {number: "CC120747254J00137188814", jobName: "java开发工程师",…}
28: {number: "CC397704085J00633603201", jobName: "大数据开发工程师",…}
29: {number: "CC579165785J00533305603", jobName: "对日开发初级技术员到项目经理的全职位招聘",…}
30: {number: "CC580898521J00578159005", jobName: "大数据高级讲师及助教",…}
31: {number: "CC554564780J00533056307", jobName: "少儿编程指导师",…}
32: {number: "CC135424103J00110711109", jobName: "大数据工程师(001576)",…}
33: {number: "CC208864430J00440666404", jobName: "爬虫工程师实习生",…}
34: {number: "CC661472022J00503449403", jobName: "数据库工程师",…}
35: {number: "CC825622670J00386054604", jobName: "大数据开发工程师",…}
36: {number: "CC376764819J00483849602", jobName: "存储/数据库架构师",…}
37: {number: "CCL1227348080J00518652901", jobName: "计算机老师",…}
38: {number: "CC281394020J00527628203", jobName: "初级软件研发工程师",…}
39: {number: "CC387944080J00283595601", jobName: "数据挖掘分析工程师",…}
40: {number: "CC120095625J00225364314", jobName: "大数据开发工程师",…}
41: {number: "CC342689820J00388863607", jobName: "数据库开发工程师",…}
42: {number: "CC806591020J00302319207", jobName: "赴日软件工程师",…}
43: {number: "CC195694025J00303289603", jobName: "中级软件工程师",…}
44: {number: "CC132366579J00325873502", jobName: "软件工程师(BSP，驱动，网络协议，网络应用，SDN方向)2020应届生",…}
45: {number: "CC506739587J00134036407", jobName: "大数据开发工程师",…}
46: {number: "CC340780835J00110537604", jobName: "开发运维工程师",…}
47: {number: "CC566973936J00094817802", jobName: "IDE开发工程师",…}
48: {number: "CC269501030J00225940408", jobName: "高级安全工程师",…}
49: {number: "CC489241831J00291329208", jobName: "大数据开发工程师",…}
50: {number: "CC449834034J00347441404", jobName: "软件工程师（深度相机）",…}
51: {number: "CC577146825J00610634701", jobName: "大数据开发工程师",…}
52: {number: "CC450090724J00427046301", jobName: "测试工程师",…}
53: {number: "CC688735724J00273153205", jobName: "上位机软件开发工程师",…}
54: {number: "CC657857520J00303388501", jobName: "数据工程师（图像算法工程师助理）",…}
55: {number: "CC312756516J00371062904", jobName: "软件开发工程师（MFC，Qt界面）",…}
56: {number: "CC198709126J90252520000", jobName: "大数据研发工程师",…}
57: {number: "CC846447660J00384107307", jobName: "后台高级开发工程师",…}
58: {number: "CC377207419J00155397111", jobName: "hadoop工程师",…}
59: {number: "CC449834034J00278985104", jobName: "软件工程师（工业机器人集成组）",…}
60: {number: "CC205108417J00469128602", jobName: "软件开发工程师-智慧城市-合肥",…}
61: {number: "CC653633480J00641775205", jobName: "后端研发工程师",…}
62: {number: "CC846538580J00299632203", jobName: "某企业ＢＩ工程师（甲方）",…}
63: {number: "CC120609234J00195014509", jobName: "大数据建模助理-实习",…}
64: {number: "CC449834034J00296268004", jobName: "机器人软件系统工程师",…}
65: {number: "CC465952081J90250044000", jobName: "大数据工程师",…}
66: {number: "CC204285426J00296918307", jobName: "高级软件工程师",…}
67: {number: "CC198713022J90251795000", jobName: "软件工程师",…}
68: {number: "CC653633480J00641772005", jobName: "大数据开发工程师",…}
69: {number: "CC714710180J00507566803", jobName: "逆向开发工程师",…}
70: {number: "CC000421286J00564655801", jobName: "大数据工程师",…}
71: {number: "CC400246730J00363422502", jobName: "大数据开发工程师",…}
72: {number: "CC204285420J00149592007", jobName: "工业软件工程师",…}
73: {number: "CC557847320J00627311805", jobName: "大数据开发工程师",…}
74: {number: "CC568312428J00256667503", jobName: "高级软件工程师",…}
75: {number: "CC493120425J00060735503", jobName: "大数据工程师",…}
76: {number: "CC192745913J00114147309", jobName: "浏览器研发工程师",…}
77: {number: "CC199736025J00394987803", jobName: "智能软件工程师",…}
78: {number: "CC205108417J00426077202", jobName: "爬取资源工程师-核心研发平台-合肥",…}
79: {number: "CC819764980J00182458203", jobName: "数据开发工程师",…}
80: {number: "CC881755400J00586559805", jobName: "大数据开发工程师",…}
81: {number: "CC223508426J00387040602", jobName: "大数据(平台)工程师",…}
82: {number: "CC839535710J00200691911", jobName: "软件工程师",…}
83: {number: "CC205108417J00382518802", jobName: "安全工程师-渗透测试（技术中心）",…}
84: {number: "CC315847111J00139550913", jobName: "Hadoop开发工程师-合肥-01760",…}
85: {number: "CC876522040J00539137305", jobName: "赴日IT工程师",…}
86: {number: "CC305515434J00457147408", jobName: "大数据流计算开发工程师",…}
87: {number: "CC205108417J00304174702", jobName: "云计算工程师-核心研发平台",…}
88: {number: "CC315847111J00077759513", jobName: "Hadoop开发工程师-合肥-01450",…}
89: {number: "CC205108417J00308369802", jobName: "引擎与算法测试工程师",…}


"""
import requests
import json
from bs4 import BeautifulSoup

url = "https://sou.zhaopin.com/?jl=664&kw=python&kt=3"

baseurl = "https://fe-api.zhaopin.com/c/i/sou?at=d92105e8cae54d02a1987d178d69e859&rt=7617e6248f1f4895a99f8fb965c4673a&_v=0.37024268&x-zp-page-request-id=b2cf5f4a9496431faccfb73c0f24f0a9-1589635687879-904128&x-zp-client-id=124efcfb-75b3-486c-fa70-1257e3df575e&MmEwMD=5jGCM7d8iqtr_5DhLemfxXFGQfsw.dqyf_tK0Wv9FqRf42r42djOGDFDQ4tLXW4db3H2.rl1Wq_box36DF8.nMzxYZC7slHR.injVuS0OBnehXjJ1ISRWPF3ub4oCtggFjLVKfdujvZTlWJSMhKtb9EAAr2VvCPzIfdkvZ7FBwzwXlpT_v.TfFP8dK0BgsgtiYpmpvaqpEXp74yZEKFFhG12YAB3rH3Yjw0C1Fz0pkpEKlUnSwJCgFdZsSAPZVkuPW6VBo0F28NTCYqnu5a6ZW7_AUrC1WySCzaeFNLUhgxiYMElYrodRXYrel1dC9iO1goNNhnqQz34NGNT3mcZt1MR9v0JJM_Z_SHm7GEcyyVCassGdMpMqVQs06qPoCYZ5rfzDLIiJPwP8xhvpKSeHLACz"

# data = {
#     "jl": "664",
#     "kw": "python",
#     "kt": "3"
# }
#
headers = {
    #"content-length": len(data),
    "content-type": "application/json;charset=UTF-8",
    "cookie": "x-zp-client-id=124efcfb-75b3-486c-fa70-1257e3df575e; adfcid2=none; adfbid2=0; sts_deviceid=1715e6aaf3a224-055235fc05655d-5313f6f-1327104-1715e6aaf3b32a; dywez=95841923.1586426982.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; __utmz=269921210.1586426982.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dywea=95841923.4348437074862309400.1586426982.1586426982.1587134994.2; __utma=269921210.680751055.1586426982.1586426982.1587134995.2; jobRiskWarning=true; urlfrom2=121113803; urlfrom=121113803; adfbid=0; sts_sg=1; sts_sid=1721d9c057eb3-0eb8a974ac8624-d373666-1327104-1721d9c057f3f0; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAaNWb0ckVM0KqiAsKW4oqX0000058OX7C00000X5cxJy.THLyktAJdIjA80K85yF9pywd0ZnqujmLmvmsnjmsnj04PWDLnsKd5RRsfHPAPHnsPbDYwHNanHDYnDDzrHT1nWbsrj-DPjFA0ADqI1YhUyPGujY1n1RsnjTvPW6vFMKzUvwGujYkP6K-5y9YIZK1rBtEmv4YQMGCmyqspy38mvqVQYd9ThV-IaqLpAq_uNqWULN8IANzQhG1Tjq1pyfqnHcknHD1rj01FMNzUjdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHqdIAdxTvqdThP-5yF9pywdTAPsXBudIAdxUyNbpgNV5yPsIaudIAdxmvq8IAN8IjdsmLKlFMNYUNqWmydsmy-MUWdsmzdBpy7EIAb0mLFW5HDkPHD1%26tpl%3Dtpl_11534_22213_17382%26l%3D1517862907%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3350076686_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D234%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26rqlang%3Dcn; at=d92105e8cae54d02a1987d178d69e859; rt=7617e6248f1f4895a99f8fb965c4673a; acw_tc=ac11000115896346966296490e010852a686b4a1bd5504fc791c7a8e78c185; ZP_OLD_FLAG=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221072823302%22%2C%22%24device_id%22%3A%221715e6aaf4e203-04162f2b20af33-5313f6f-1327104-1715e6aaf4fb2e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAaNWb0ckVM0KqiAsKW4oqX0000058OX7C00000X5cxJy.THLyktAJdIjA80K85yF9pywd0ZnqujmLmvmsnjmsnj04PWDLnsKd5RRsfHPAPHnsPbDYwHNanHDYnDDzrHT1nWbsrj-%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%221715e6aaf4e203-04162f2b20af33-5313f6f-1327104-1715e6aaf4fb2e%22%7D; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1587134995,1589634699; LastCity=%E5%90%88%E8%82%A5; LastCity%5Fid=664; privacyUpdateVersion=3; POSSPORTLOGIN=0; CANCELALL=1; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%22def1d4f5-b0b0-4c8f-a835-ff15d03ba0f8%22%2C%22funczone%22:%22addrsm_ok_rcm%22}%2C%22sou%22:{%22actionid%22:%22d7dd7106-ee55-4369-941e-3053b3431bf8-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=21; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1589635690",
    "origin": "https://sou.zhaopin.com",
    "referer": "https://sou.zhaopin.com/?jl=664&kw=python&kt=3",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

rsp = requests.post(url=baseurl).json()

print(rsp)












