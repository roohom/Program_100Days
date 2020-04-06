# 前端学习笔记

### From DAY 06

### 在页面中引用一段话可以使用&#60;q&#62;&#60;/q&#62;和&#60;blockquote&#62;&#60;/blockquote&#62;元素
其中：
~~~
<q></q>用来标记短的引用
而
<blockquote></blockquote>标记长的引用
。
~~~
当使用上述两个元素时，浏览器会自动将元素里的内容加上双引号（有的浏览器则是另外的标记），&#60;q&#62;&#60;/q&#62;为&#60;p&#62;&#60;/p&#62;段落里的具体某个词语或者一小句话添加双引号，
而&#60;blockquote&#62;&#60;/blockquote&#62;为其内的一个或多个段落添加双引号，表示长引用。

要想使得语句换行可以使用&#60;br&#62;,它是一个元素  
但是所谓的**元素定义**是
~~~
开始标记+内容+结束标记
~~~
为什么它还能被称之为元素呢，因为在实际运用中，它仅表示换行，其间不需要加任何内容，再写结束标记岂不是降低效率吗，为此直接精简，就只写开始标记即可，实际上，它的原样为  
&#60;br&#62;----&#60;/br&#62;  
它有一个专门的名称----void元素。&#60;br&#62;和&#60;img&#62;都是void元素。


### 列表
~~~
unorder list = ul
order list = ol
list item = li
~~~

实例：
~~~
html
<p>
<ol>
    <li> First</li>
    <li> <em>Second</em></li>  <em></em>用来将内容文本设置斜体
</ol>
</p>
~~~
<p>
<ol>
    <li> First</li>
    <li> <em>Second</em></li>
</ol>

其他两个列表使用类似，当然，你也可以随意嵌套，只要符合规范即可。

### 嵌套关系
~~~
     
    - head - title
HTML
    - body - p - q
                      
~~~

### DAY 06 append

#### 在web上发布自己的网站需要做以下几件事：
~~~
1.找一家托管公司
2.为网站起一个名字
3.想办法把文件从自己的计算机上传到托管公司的服务器上（FTP）
4.公开网站地址
~~~

#### 细节:
```
1.买一个域名 
2.买一个服务器（比如阿里云的轻量服务器，需要做的最麻烦的工作是备案）
3.将网站文件上传到服务器(FTP)
另一种方法:
1.将所编写的网站所需文件上传到GitHub仓库，将仓库名命名为username.github.io
2.直接在浏览器输入地址username.github.io即可直接访问网站，index.html为网站主页
3.购买一个域名，将域名的A和CNAME指向username.github.io即可实现用域名访问你的网站
```
#### FTP命令:
```html
dir:得到当前目录的文件夹
cd:切换到另一个目录，“..”也表示上一层目录
pwd:显示当前目录
put<filename>:将指定的文件夹上传到服务器
get<filename>:从服务器获取指定的文件，传回到你的计算机
```
#### 默认页面:
- 当你在地址栏键入你的网址并按下回车时，WEB服务器接收到请求，它会查找找个目录中的一个默认文件。
- 通常默认文件名为“index.html”或“default.htm”，如果服务器找到这样一个文件，就会把它返回给浏览器显示。

#### 链接到其他网站
方法：  
只要知道你所要链接到的其他网站的URL（统一资源定位符，Uniform Resource Locator）,再把这个URL放在&#60;a&#62;元素中作为href属性值即可。

### DAY 07
#### 设置文字水平和上下居中
~~~html
.box{
    text-align:center;                                  设置水平方向居中
    line-height:100px;(根据实际大小指定，满大小为垂直居中)    设置垂直方向居中
}
~~~

#### 块元素,内联元素,内联块元素之间的转换

display属性是用来设置元素的类型及隐藏的，常用的属性有：
~~~
1、none 元素隐藏且不占位置

2、block 元素以块元素显示

3、inline 元素以内联元素显示

4、inline-block 元素以内联块元素显示
~~~
可以通过这样的示例实现当鼠标移至元素上时，显示内容，当鼠标移走时，隐去内容:
~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>元素的隐藏和显示</title>
    <style>
        
        .box3{
            width: 200px;
            height: 200px;
            background: green;
        }
        .box3 span{
            display:none;
        }
        /*当我鼠标移入box3的时候让字体显示*/
        .box3:hover span{
            color:pink;
            text-align:center;
            line-height:200px;
            font-size:30px;
            display:block;
        }
    </style>
</head>
<body>
    <div class="box1">box1</div>
    <div class="box1 box2">box2</div>

    <div class="box3">
        <span>我显示了</span>
    </div>
</body>
</html>
~~~
其效果类似于一些网页上当鼠标移动到上面时显示内容，移走又隐藏内容(京东、淘宝的选择购物板块、网易云课堂的课程内容板块).

## DAY 08

### 浮动和定位

*插曲*：

~~~~html
元素与页面边框默认有一个8px的边距，想删除这个边距的解决办如下：
使用通配符*
在style元素中加入以下代码：
*{margin：0； padding：0}
即可
~~~~

文档流：

~~~~
文档流，是指盒子模型按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，行元素在一行之内从左到右排列，先写的先排列，后写的排在后面，每个盒子都占据自己的位置。
~~~~



#### 浮动



#### 定位

使用**position**来对元素进行定位

定位方法有以下四种：

~~~~html
1.relative 
args(left, right)
相对定位，以元素本身定位作为参考点进行偏移；不会脱离文档流
生成相对定位元素，元素所占据的文档流的位置不变，元素本身相对文档流的位置进行偏移
2.absolute 
args(left, right)
绝对定位，以父级为参考点进行偏移，若父级没有定位则以父级的上一级为参考，没有则继续向上寻找，直到找到body级；会脱离文档流，不占文档位置
生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于上一个设置了相对或者绝对或者固定定位的父级元素来进行定位，如果找不到，则相对于body元素进行定位。
3.fixed 
args(left, right)
绑定定位，以浏览器窗口为参考进行定位
主要用在:固定在头部的导航栏，返回顶部、网页的侧边栏菜单
4.static
默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性
~~~~

实例：

绑定定位可以轻松制作网页上**返回顶部**的按钮



## DAY 09

### 页面布局

#### 响应式布局

**媒体查询**

当浏览器窗口大小变化时，页面自动适应窗口大小做出调整。

~~~~
响应式布局：创建多个布局，分别对应一个屏幕分辨率范围

特点：分别为不同的屏幕分辨率定义布局，同时，在每个布局中，应用流式布局的理念，即页面元素宽度随着窗口调整而自动适配

响应式布局就是使用媒体查询的方式,创建多个元素宽度是相对的的布局理想的响应式布局是指的对PC/移动各种终端进行响应的
~~~~

伪代码如下：

~~~~html
.a{
   height: 200px;
   display: inline-block;
}
/*当浏览器窗口小于=960时*/
@media (max-width:960px){
    .a{width:50%;}
}
/*当浏览器窗口小于=640时*/``_****_``
@media (max-width:640px){
    .a{width:100%;}
}
/*当浏览器窗口大于等于960时*/
/*@media (min-width:960px){
    .a{width:25%;}
}*/

~~~~

# JavaScript

#### 什么是JavaScript？

JavaScript是运行在浏览器端的脚步语言，JavaScript主要解决的是前端与用户交互的问题，包括使用交互与数据交互。JavaScript是浏览器解释执行的

~~~~
JavaScript 是一种客户端脚本语言（脚本语言是一种轻量级的编程语言）
JavaScript 通常被直接嵌入HTML页面。
JavaScript 是一种解释性语言
~~~~

**特点：**

~~~~
1. 弱类型 
2. 基于对象。(因为面向对象需要具有封装、继承、多态的特征)
3. 安全
4. 兼容性
~~~~

#### JavaScript嵌入页面的方式

1、页面script标签嵌入

```
<script type="text/javascript">


    var a = '你好！';
    alert(a);


</script><input type="button" name="" onclick="alert('ok！');">
```

2.外部引入

```
<script type="text/javascript" src="js/index.js"></script>
```

3.行间事件（主要用于事件）

```
<input type="button" name="" onclick="alert('ok！');">
```

JavaScript语句与注释**

1、一条JavaScript语句应该以“;”结尾

2、JavaScript注释

```
// 单行注释
var a = 123;
/*  
    多行注释
    1、...
    2、...
*/
```

### JavaScript变量

```
JavaScript 是一种弱类型语言，javascript的变量类型由它的值来决定。

定义变量需要用关键字 'var',

不使用var关键字定义全局变量在严格模式下将会执行错误 "use strict";
```

```
var a = 123;
 var b = 'asd';

 //同时定义多个变量可以用","隔开，公用一个‘var’关键字

 var c = 45,d='qwe',f='68';
```

**变量,函数,属性命名规范**

```
字母数字下划线($)
首字母不能为数字
严格区分大小写
不能使用关键字
```

### JavaScript 基本数据类型

typeof函数获取一个变量的类型：

```angularjs
* boolean - 如果变量是 Boolean 类型的
* number - 如果变量是 Number 类型的 (整数、浮点数)
* string - 如果变量是 String 类型的 （采用""、 ''）
* object - 如果变量是一种引用类型或 Null 类型的 
        如：new Array()/ new String()...
* function -- 函数类型
* undefined - 如果变量是 Undefined 类型的
```

### js数据类型转换

使用：Number（）、parseInt() 和parseFloat（） 做类型转换

```angularjs
Number()强转一个数值(包含整数和浮点数)
*parseInt()强转整数
*parseFloat（）强转浮点数

当字符串中包含任意一个非数值表示的字符时：
Number() 返回NaN\
parseInit(),parseFloat() 从头开始往后读，如果碰到非数值表示的字符时，就舍去后面的字符，前面的整数返回为整数，浮点数返回为浮点数。比如‘1.a234abc’ parseInit()返回1，parseFloat()返回1.234
```

函数isNaN()检测参数是否不是一个数字。

```angularjs
isNaN()  is not a number
```

可用的 3 种强制类型转换如下：

```angularjs
Boolean(value) - 把给定的值转换成 Boolean 型；

Number(value) - 把给定的值转换成数字（可以是整数或浮点数）；

String(value) - 把给定的值转换成字符串；
```

### js运算符

算术运算符

```angularjs
 + - * / ++ --
```

字符串连接

```angularjs
 +
```

赋值运算

```angularjs
 =    +=   -=   %=
```

比较运算符

```angularjs
<  >    >=    <=  
==   (等，允许等号两边数据类新不一样，解释器会自动做强制类型转换，1==‘1’ 返回true)
===  (全等，两边除了数值相等，数据类型也必须相同)
!=   (不等，不需要判断两边的类型)
!==  (全部等，需要判断等号两边数据的类型)
```

逻辑运算符

```angularjs
 &&  ||  !
```

位运算

```angularjs
 ^    &    |   <<   >>
```

其它运算符

```angularjs
?   :    三元运算符
```