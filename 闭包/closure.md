# 闭包函数
>既然可以把函数作为一个形参进行传递，作为回调函数，那么如果在一个函数中，返回一个函数，则成为闭包函数
>在一个函数内，返回了一个内函数，并且返回的函数还使用了外函数中的局部变量，这就是闭包函数
闭包的特点:
    1. 在外函数中定义了局部变量，并且在内部函数中使用了这个局部变量
    2. 在外函数中反悔了内函数，返回的内函数就是闭包函数
    3. 主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏


~~~~Python
def person():
    money = 0

    # 工作     在外函数中定义的内函数
    def work():
        nonlocal money  # 在内函数中使用了外函数的临时变量
        money += 100
        print(money)

    # # 加班
    # def overtime():
    #     global money
    #     money += 200
    #
    # # 购物
    # def buy():
    #     global money
    #     money -= 50

    # 在外函数中返回了内函数，这个内函数就是闭包函数
    return work


res = person()   # return work   res = work
res()
res()
# 此时就不能能在全局中对money这个局部变量进行任何操作了
# 闭包的作用: 保护了函数中的变量不受外部的影响，但是又能不影响使用


# 如何检测一个函数是否为闭包函数:    函数名.__closure__ ，如果是闭包函数返回的是cell，如果不是返回none
print(res.__closure__)
print(person.__closure__)
~~~~