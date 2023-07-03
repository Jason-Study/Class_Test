#!/usr/bin/python3
# 菜鸟教程：https://www.runoob.com/python3/python3-class.html

# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

class Site:
    def __init__(self, name, url):
        self.name = name  # 公共变量
        self.__url = url  # 私有变量

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法  只能在类的内部调用 ，不能在类的外部调用
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')  # 实例化类
x.who()  # 正常输出
x.foo()  # 正常输出
x.__foo()  # 报错
