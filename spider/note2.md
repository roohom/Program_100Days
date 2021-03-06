# 页面解析和数据提取
- 结构数据:先有的结构，再谈数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作(json类)
    - XML文件
        - 转换成Python类型(xml to dict)
        - XPath
        - CSS选择器
        - 正则    
- 非结构化数据:先有数据，再谈数据
    - 文本
    - 电话号码
    - 邮箱地址
        - *通常处理这一类数据，使用正则表达式*
    - HTML文件
        - 正则
        - XPath
        - CSS选择器
   
# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
- 案例v21,re的基本使用流程
- 案例v22,match的基本使用
- 正则常用方法:
    - match:从开始位置开始查找，一次匹配
    - search:从任何位置开始查找，一次匹配   案例v22
    - findall:全部匹配，返回列表 案例v23
    - finditer:全部匹配，返回迭代器
    - split:分割字符串，返回列表
    - sub:替换
- 匹配中文
    - 中文Unicode范围主要在[u4e00-u9fa5]
    - 案例v24    
    
-贪婪与非贪婪
    - 贪婪模式:在整个表达式都匹配成功的情况下，尽可能多地匹配
    - 非贪婪模式:在整个表达式都匹配成功的情况下，尽可能少地匹配
    - Python里的数量词默认是贪婪模式
    - 例如:
        - 查找文本abbbbbbccc
        - re是ab*
        - 贪婪模式:abbbbbb
        - 非贪婪:结果是a
# XML
- XML(ExtensibleMarkupLanguage)
- http://www.w3school.com.cn/xml/index.asp
- 案例v25.xml
- 概念:父节点，子节点，先辈节点，兄弟节点，后代节点

# XPath
- XPath(XML Path Language),是一门在XML文档中查找信息的语言。
- 官方文档:http://www.w3school.com.cn/xpath/index.asp
- XPath开发工具
    - 开源的XPath表达式工具:XMLQuire
    - chrome插件:XPath Helper
    - Firefox插件:XPath Checker
    
- 常用路径格式
    - nodename:选取选取此节点的所有子节点
    - /:从根节点开始
    - //:选取元素，而不考虑元素的位置
    - .:当前节点
    - ..:父节点
    - @:选取属性
    - 案例:
        - bookstore:选取bookstore的所有子节点
        - /bookstore:选取根元素
        - bookstore/book:选取bookstore的所有为book的子元素
        - //book:选取book子元素
        - //@lang:选取名称为lang的所有属性
- 谓语(Predicates)
    - 谓语用来查找某个特定的节点，被镶嵌在方括号中
    - /bookstore/book[1]:选取第一个属于bookstore下叫book的元素
    - /bookstore/book[last()]:选取最后一个属于bookstore下叫book的元素
    - /bookstore/book[last()-1]:选取倒数第二个属于bookstore下叫book的元素
    - /bookstore/book[position()<3]:选取属于bookstore下叫book的前两个元素
    - /bookstore/book[@lang='cn']:选取属于bookstore下叫book的,含有属性lang的值是cn的元素
    - /bookstore/book[@price < 90]:选取最后一个属于bookstore下叫book的，含有属性price的，且值小于90的元素
    
    
- 通配符
    - '*':任何元素节点
    - @*:匹配任何属性节点
    - node():匹配任何类型的节点
    
- 选取多个路径
    - //book/title | //book/author :选取book元素中的title和author元素
    - //title | //price: 选取文档中所有的title和price元素
    
# lxml
- Python的HTML/XML的解析器
- 官方文档: http://lxml.de/index.html
- 案例v26
- 功能:
    - 解析HTML
    - 文件读取 案例v27.html, v28.py
    - etree和XPath配合使用,案例v29
    
# CSS选择器 BeautifulSoup4    
- 当前得版本是bs4
- 官网: http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
    - 正则，很快，不好用，无需安装
    - beautifulsoup，慢，使用简单安装简单
    - lxml，比较快，使用简单，安装一般
- 案例v30
- 四大对象
    - Tag
    - Navigator
    - BeautifulSoup
    - Comment
- Tag
    - 对应的Html中的标签
    - 可以通过soup.tag_name
    - Tag两个重要属性
        - name
        - attrs
    - 案例v31
    
- NavigableString
    - 对应内容值
- BeautifulSoup
    - 表示的是一个文档的内容，大部分可以把他当做tag对象
    - 一般可以用soup来表示
- Comment
    - 特殊类型的NavigableString对象
    - 对其输出，内容不包括注释符号
    
    
- 遍历一个文档对象
    - contents: tag的子节点以列表的方式给出来
    - children:子节点以迭代器形式返回
    - descendents:所有的子孙节点
    - string
    -案例v32
- 搜索文档对象
    - find_all(name, attrs, recursive, text, **kwargs)
        - name:按照字符串搜索，可以传入的内容有:
            - 字符串
            - 正则表达式
            - 列表
        - kwargs参数:可以用来表示属性
        - text:对应的tag的文本值
        - attrs:传入的参数类型是**字典类型**
        - 案例v33
- CSS选择器    
    - 使用soup.select， 返回一个列表
    - 通过标签名称:soup.select("title")
    - 通过类名:soup.select(".content")
    - id查找:soup.select("#name_id")
    - 组合查找:soup.select("div #input_content")
    - 属性查找:soup.select("img[class='photo']")
    - 获取tag内容:tag_get_text
    - 案例v34

# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
- 案例v35



