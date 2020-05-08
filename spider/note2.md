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
    - 例如
        - 查找文本abbbbbbccc
        - re是ab*
        - 贪婪模式:abbbbbb
        - 非贪婪:结果是a
# XML
- XML(ExtensibleMarkupLanguage)
- http://www.w3school.com.cn/xml/index.asp
- 案例v25.xml
- 概念:父节点，子节点，先辈节点，兄弟节点，后代节点