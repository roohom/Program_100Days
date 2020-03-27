# 前端笔记Day 05
前言：
今天妈妈回来，刚开始必定有很多杂事，所以白天就没有了学习时间。没有看新一篇的前端课程视频，但是今天拿到了新买的《Head First HTML&CSS》,拿到手就看了一些，记下这些。

### 正文
在HTML中引用CSS，将CSS插入到Head头中，并用Style包围。
比如：
~~~
CSS
~~~
~~~
<style type="text/css">
    body{
    background-color:#ccc;         背景颜色
    margin-left:20%;       左右边距分别占页面的20%
    margin-right:20%;
    border:2px dotted black;     定义页面主题周围的边框是虚线，颜色为黑色
    padding:10px 10px 10px 10px;     在页面主题周围创建一些内边距
    font-family:sans-serif;        定义页面文本使用的字体
    }
</style>
~~~
之前一直看到一些论坛和博客的页面就是左右有边距，刚开始看HTML的时候就好奇怎么实现这个样式，原来如此简单。

详情看我写了一个简单的测试案例。