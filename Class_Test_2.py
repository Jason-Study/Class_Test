#!/usr/bin/python3
# 来自菜鸟教程：https://www.runoob.com/python3/python3-class.html

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1  # 私有方法
        self.publicCount += 1  # 公开方法
        print(self.__secretCount)


counter = JustCounter()  # 实例化类
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量
