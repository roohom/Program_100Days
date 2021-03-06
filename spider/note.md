# 一些笔记

- 爬虫三个步骤:
    1. 把页面down下来
    2. 把页面数据提取出来
    3. 把页面里面下一个网址找到，再重复以上


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
- cookie & session
    - 由于http协议的无记忆性，为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发给用户(即http浏览器)的一段信息，session是保存在服务器上的另一半
    信息，用来记录用户信息
    - 区别:
        - 存放位置不同
        - cookie不安全
        - session会保存在服务器上一定时间，会过期
        - 单个cookie保存数据不超过4K，很多浏览器限制一个站点最多保存20个
    - session的存放位置
        - 存放在服务器端
        - 一般情况，session是放在内存中或者数据库中 
        - 没有cookie登录，反馈的网页是未登录状态
    - 使用cookie登录
        - 直接把cookie复制下来，然后手动放入请求头中   
        - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
            - CookieJar
                - 管理存储cookie，向传出的http请求添加cookie
                - cookie存储在内存中，CookieJar实例回收后cookie将消失
            - FileCookieJar(filename, delayload=None, policy=None):
                - 使用文件管理cookie
                - filename是保存cookie的文件
                    - 创建与Mozilla浏览器cookie.txt兼容的FileCookieJar实例
            - LwpCookieJar
                - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookie.Jar实例
            - MozillaCookieJar
            - 他们的关系是：Cookie->FileCookieJar->MozillaCooikieJar & LwpCookiJar
        - 利用Cookie.Jar访问人人，案例v10
            - 自动使用cookie登录：
            - 打开登录页面后自动通过用户名密码
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登录隐私页面
        - handler是Handler的实例，常用参看代码
            - 用来处理复杂请求
                # 生成cookie的管理器
                cookie_handler = request.HTTPCookieProcessor(cookie)
                # 创建http请求管理器
                http_handler = request.HTTPHandler()
                # 生成https管理器
                https_handler = request.HTTPSHandler()
                
        - 创立handler之后，使用opener打开，打开之后相应的业务由相应的handler处理
        - cookie作为一个变量打印出来，案例v11
            - cookie的属性
                - name:名称
                - value: 值
                - domin: 可以访问此cookie的域名
                - path: 可以发现此cokie的页面路径
                - expires:过期时间
                - size:大小
                - Http字段
        - cookie的保存-FileCookieJar，案例v12
        - cookie的读取
            - 案例v13
- SSL
    - SSL证书是什么？ - 是指遵守SSL安全套阶层协议的服务器数字证书(SecureSocketLayer)
    - 美国网景公司开发
    - CA(CertificateAuthority)是数字证书认证中心发放、管理、废除数字证书的收信人的第三方机构
    - 遇到不信任的SSL整数，需要单独处理(忽略)，案例v14
    
- JS加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理(通常是取MD5值)
    - 经过加密，传输的就是密文，但是加密函数或过程一定是在浏览器完成，也就是一定胡巴代码(js代码)暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 案例v15
    
- ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般使用json格式
    - 案例v16，爬取豆瓣电影
        
# Requests，献给人类
- HTTP for Humans,更简洁更友好
- 继承了urllib的所有特性
- 底层使用的是urllib3
- 开源
- 中文文档
- 安装: conda install requests
- get请求
    - request.get()    
    - requests.request("get", url)
    - 可以带有headers和params参数
    - 案例v18
    
- get返回内容
    - 案例v19
- post
    - rsp = requests.post(url, data=data)
    - data、headers要求是dict类型
    - 案例v20
    
- proxy
         proxies = {
         "http": "address of proxy",
         "https":"address of proxy"
         }
         
         rsp = requests.request('get','http:xxxx','proxies=proxies')
    - 代理可能会出错，如果使用人数过多，考虑安全问题，可能会被强行关闭
    
- 用户验证
    - 代理验证   
            # 可能需要使用使用HTTP basic Auth
            # 格式为 用户名:密码
            proxy = { "http":"china:123456@192.168.123:4444"} 
            rsp = requests.get("http://baidu.com", proxy=poxy)
- web客户端验证
    - 如果需要web客户端验证，需要添加：auth=(用户名，密码)    
        auth=("test1", "12345") # 授权信息
        rsp = requests.get("http://www.baidu.com", auth=auth)

- cookie
    - requests可以自动处理cookie信息
    
            rsp = requests.get("http://xxxxxxxx")        
            # 如果对方服务器穿送过来cookie信息，则可以通过反馈的cookie属性得到
            # 返回一个cookieJar实例
            cookiejar = rsp.cookies
            
            # 可以通过cookiejar转换成字典
            cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
            
            
- session
    - 跟服务器端session不是一个东西
    - 模拟一次绘画，从客户端浏览器链接服务器开始，到客户端浏览器断开
    - 能让我们跨请求时保持某些参数，比如在同一个session实例发出的所有请求之间保持cookie   
            # 创建session对象，可以保持cookie值
            se = requests.session()
            headers = {"UserAgent":"xxxxxxxxx"}
            data = {"name": "xxxxxxxx"}
            
            # 此时，由创建的session管理请求,负责发出请求
            ss.post("http://www.baidu.com", data=data, headers=headers)
            rsp = ss.get("xxxxxxxx")
            
- Https请求验证ssl证书
    - 参数verify负责表示是否需要验证ssl证书，默认是True
    - 如果不需要验证ssl证书，则设置成False表示关闭       
    
            rsp  requests.get("https://www.baidu.com", verify=False)
            # 如果用verify=True访问12306，会报错，因为他证书有问题
    
    
        