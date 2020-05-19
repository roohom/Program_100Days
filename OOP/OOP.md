# OOP
- 思想
    - 以模块化思想解决工程问题
    - 面向过程vs面向对象
    - 由面向过程转向面向对象
    - 举个栗子，开一所学校，组成:
        - 讲师
        - 学生
        - 班主任
        - 教室
        - 学校
- 常用名词
    - OO: 面向对象
    - OOA:分析
    - OOD:设计
    - OOP:编程
    - OOI:实现
    - OOA-> OOD-> OOI
- 类vs对象
    - 类:抽象，描述的是一个集合，侧重于共性
    - 对象:具象，描述的是个体  
- 类的内容:
    - 动作，函数
    - 属性，变量
- 定义类: class关键字
- 类命名:
    - 遵循大驼峰
    - 第一个字母大写    
    
    
    
## 定义学生类和几个学生
~~~~Python
class Student():
    # 此处定义一个空类
    pass     

~~~~
## 定义一个对象
xstu = Student() 括号里可以为空也可以接收参数，根据你定义的类

~~~~Python
class PythonStudent():
    name = 'NoOne'
    age = 18
    course = "Python"
    
    # 动作即是函数，函数即是动作
    # 定义类中的函数
    # 一般需要self关键字
    # 其余跟普通函数基本相同
    def myFunc():
        pass

xiaobai = PythonStudent()    
print(xiaobai.name)    
print(xiaobai.age)

~~~~
  
  
# 类的属性
## 类的例子
## 注意类的定义

~~~~Python
class Student():
    name = '王三屎‘
    age = 19

    def sayHi(self):
        print("hello!")  
        # 如果没有return会返回什么
        return None
~~~~

- 实例化
~~~~Python
er_na = Student()
print(er_na)
~~~~

# self
- self可以用别的名称来代替
- self不是关键字
- 作用是指代本身
    - 栗子
    
- self栗子
- 实例调用函数
~~~~Python
yaoyao = Student()

# 调用yaoyao的动作
# 调用没有使用参数
# 默认实例作为第一个参数传入
yaoyao.sayHi()

~~~~

## 类的变量的作用域的问题
- 类变量: 属于自己的变量
- 实例变量: 属于实例的变量
- 访问实例的属性，如果实例没有定义属性，则自动访问类的属性，如果类也没有定义则会报错


~~~~Python
class Student():
    # name、age是类的变量
    # 注意类的变脸的定义位置和方法
    # 不需要前缀
    name = 'wangsnashi'
    age = 19
    
    def sayHi(self, n, a):
        self.name = n
        self.age = a
        return None

# 类的变量可以被实例变量借用
~~~~


## 访问类的属性
- 在类里如果强制访问类的属性，则需要使用__class__,(注意前后的下划线)
- 类方法: 
    - 定义类的方法的时候，没有self参数
    - 类的方法中只允许使用类的内容
    - 两种方法
        -  ClassNmae
        - __class__
        
## 构造函数
- 类在实例化的时候，执行一些基础新的初始化的工作
- 使用特殊的的名称和写法:
    - ~~~~Python
      def __init__(self):
          print("我是构造函数")
      ~~~~
- 在实例化的时候自动执行
- 是在实例化的时候"第一个"被执行的函数



## 面向对象的三大特征
- 继承
- 封装
- 多态

### 继承
- 子类可以使用父类定义的内容或者行为等
- 继承的实现:
    - 父类，基类，被继承的类，Base Class,Super Class
    - 子类，有继承行为的类
    - 所有类都必须有一个父类
        - 如果没有，则默认是object的子类
        - 子类可以有多个父类
        - ~~~~Python
        class  Person():
            pass
            
            # 父类写在类定义的时候的括号里
        class Teacher(Person):
            pass                                 
        ~~~~

### issueclass检测是否为子类
- 可以用来检测两个类的父子关系
    - 使用~~~~
    issueclass(类名，类名)
    ~~~~
### 构造函数的继承
- 构造函数默认继承
- 一旦子类定义了构造函数，则不再自动调用父类的构造函数
~~~~Python
class Person():
    def __init__(self):
        pass

class Teacher(Person):
    pass
~~~~        













    
    
           