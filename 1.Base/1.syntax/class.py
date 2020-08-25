class Base:
    def __init__(self):
        self.base = 0

class Child(Base):
    # 如果子类重新实现了__init__则需要在这里调用父类的构造函数,如果没有重写__init__会自动调用父类的构造函数
    def __init__(self):
        super().__init__()  #这里可以写成 Base.__init__(self) 注意,需要加self
        self.child = 1

test = Child()
print(test.base)
print(test.child)
