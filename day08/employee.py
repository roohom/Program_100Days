#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 22:47
# @Author  : Roohom
# @Site    : 
# @File    : employee.py
# @Software: PyCharm

"""
抽象类/方法重写/多态
实现一个工资结算系统 公司有三种类型的员工
    - 部门经理固定月薪12000/月
    - 程序员案本月工作小时数每小时100元
    - 销售员1500元/月的底薪加上本月销售额5%的提成
输入员工的信息 输出每位员工的月薪信息
"""

from abc import ABCMeta,abstractclassmethod


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractclassmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 12000


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100 * self._working_hour


class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == '__main__':
    employees = [Manager('drh'), Programmer('阿红'), Salesman('hong')]
    for emp in employees:
        if isinstance(emp, Programmer):
            working_hour = int(input("请输入%s本月工作时间：" % emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):
            sales = float(input("请输入%s本月销售额:" % emp._name))
            emp.set_sales(sales)

        print('%s本月月薪为：￥%.2f元' % (emp.name, emp.get_salary()))