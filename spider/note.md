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
		  
