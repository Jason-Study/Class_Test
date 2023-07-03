#!/usr/bin/python3
# 来自菜鸟教程：https://www.runoob.com/python3/python3-class.html

# 类定义
class People:
    """一个简单的类实例"""
    # 定义基本属性
    # i_File = 12345
    name = ''
    age = 0

    # 定义私有属性(私有变量),私有属性在类外部无法直接进行访问
    __weight = 0

    # 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
    # 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

    # 定义构造方法
    def __init__(self, n, a, w=50):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁， %d 斤。" % (self.name, self.age, self.__weight))

    def sayhello(self):
        return 'hello world'

    def prt(self):
        print(self)
        print(self.__class__)


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类People的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我现在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, a, t):
        self.name = n
        self.age = a
        self.topic = t

    # 覆写父类People的方法
    def speak(self):
        print("%s说：\"我叫”%s“，今年%d岁了。我是一名演讲家，我今天演讲的主题是%s.\""
              % (self.name, self.name, self.age, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, a, t)


# # 实例化类
# x = people()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i_File 为：", x.i_File)
# print("MyClass 类的方法 f 输出为：", x.f())
#
# t = people()
# t.prt()

# 父类对象
p = People('runoob', 10, 80)
# p.age  # 在python命令行中，能交互式显示类的属性值。在.py文件中，该行是无效行，不会输出类的属性值；输出需要用输出方法。
p.speak()
p.prt()

# 子类对象
s = Student('ken', 10, 80, 4)
s.speak()
super(Student, s).speak()  # super()函数是用于调用父类(超类)已被覆盖的方法
s.prt()
s.sayhello()

# 多继承对象
test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
test.prt()
