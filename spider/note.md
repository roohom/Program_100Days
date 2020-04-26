# 一些笔记
#### 对应图灵学院Python全栈课时59-63
- Python网络包
	- Python3.x urllib,urllib3,httplib2,requests
  
## urllib
- urllib.request: 打开和读取urls
- urllib.error： 包含urllib.request产生的常见的错误，使用try捕捉
- urllib.parse: 包含解析url的方法
- urllib.robotparse: 解析robots.txt文件
- 例子的大致流程
	- 使用urlopen打开网页，需要返回一个值，rsp = request.urlopen(url),其返回的不是str之类的对象，需要使用read()方法读取，但得到的结果仍然是bytes流，
	此时需要使用decode()方法将其转化为人能看懂得内容。
- chardet 自动侦测编码
	- 导入chardet
		- cs = chardet.detect(html)  -> cs的type为dict
- urlopen的返回对象
	- geturl: 返回请求对象的url
	- info: 请求反馈对象的meta信息
	- getcode：返回的http code (200表示OK， 404表示错误...)
- request.data的使用
	- 访问网络的两种方法
		- get:
		  - 利用参数给服务器传递信息，
		  - 参数为dict，然后用parse编码 kw = parse.urlencode(dict)
		- post
		    - 一般向服务器传递参数使用
		    - post是把信息自动加密处理
		    - 我们如果想用post信息，需要用到data参数
		    - urllib.parse.urlencode可以将字符串自动转换成：
		        - Content-Type:
		        - Content-Length:
		        - 简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
		        - 案例v01
		        - 为了更多地设置请求信息，单纯滴通过urlopen函数已经不太好用
		        - 需要利用request.Request类
		        - 案例v03
		        
- urllib.error
    - URLerror产生的原因：
        - 断网
        - 服务器连接失败
        - 找不到指定服务器
        - 是OSError的一个子类
        - 案例v04
        
    - HTTPerror， 是URLerror的一个子类
        - 案例v05
        
    - 两者区别:
        - HTTPError是对应的HTTP请求的返回状态码，400以上，引发HTTPError
        - URLError对应的一般是网络出现问题，包括url问题
        - 关系区别: OSError-URLError-HTTPError
- UserAgent 
    - UserAgent: 用户代理，简称UA，术语heads的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以**直接复制粘贴**，也可以用浏览器访问的时候抓包      
        - 百度就能搜索到
    - 设置UA值可以通过两种方式：
        - heads
        - add_header
        - 案例v06
		  
- ProxyHandler处理(代理服务器)
    - 使用代理IP，是爬虫的一个常用手段
    - 获取代理服务器的地址:
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问者，代理也不允许频繁访问一个固定网站，代理一定需要很多很多
    - 基本使用代理的步骤:
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建opener
        4. 安装opener
    - 案例v07