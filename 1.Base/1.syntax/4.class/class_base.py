
# ========================================================= base
# 所有类都有一个名为 __init__() 的函数，使用 __init__() 函数将值赋给对象属性，或者在创建对象时需要执行的其他操作
# self 参数是对类的当前实例的引用，用于访问属于该类的变量。
# 它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Bill", 63)
p1.myfunc()
# ========================================================= base end

# ========================================================= property
# 使用对象创建的属性 称之为对象属性 只有当前对象里才存在
# 如果使用对象属性创建了一个和类里面同名的属性 那么调用的时候 会优先查找对象里面的属性
# 使用类里面的方法的参数 self 创建的属性 也为对象属性
# 当使用对象.属性名来改类里面的属性的时候 其实是在对象里面创建了一个同名的属性
# 当将对象里面同名的属性删除掉以后 还是会调用类的属性
# 不能再对象里 删除 类里面的属性 只有使用的权利
# 使用类操作过的属性 所有对象在调用类属性的时候 都是修改后的属性

# 创建对象属性的方法
# class A:
#     #通过方法创建对象属性
#     def createVar(self):
#         self.xx = 'oo'
# a = A()
# #对象名.属性名
# a.name = 'xx'
# 
# 创建类属性的方法
# 类名.属性名
# ========================================================= property end


# ========================================================= priv
# (1) 类的私有属性:以 __ 作为开头 不能在类的外部进行使用和访问 在类的里面使用 self.__属性名
# 私有属性的访问
# 在类的外部： 对象._类名__属性名 查找
# 在类的内部： 方法里面的变量 self.__属性名 调用
# 
# 注意： 在类的内部只要使用self.__属性名 那么就会去找私有属性 _类名___属性名
# 
# (2) 类的私有方法
#  以 __ 作为开头 不能再类的外部进行使用和访问 在类的里面使用 self.__方法名
# 
# 在公有方法里面 通过self去调用
# ========================================================= priv end


# 静态方法
# 
# 可以在类的实例化成对象来调用 可以使用类名来调用
# 
# 实例
# class A:
#     @staticmethod
#     def demo():
#         print('类来调用')
# a = A()
# a.demo()
# A.demo()


# 常用的属性
# __doc__ 类的说明
# __name__返回类名
# __base__ 返回一个父类
# __bases__ 返回多个父类
# __dict__ 返回对象或者类的信息


# 魔术方法
# __init__ 构造方法 作为类的初始化
# __del__ 析构方法 在当前文件执行完毕之前去执行 或者是使用 del 对象名 去触发
# __str__ 用于转换成 人类能够阅读的形式
# __repr__ 转换成解释器查看的形式
# __add__ 运算符重载
# __getattr__ 调用不存在的属性的时候触发
# __len__
# __getitem__
# __setitem__
