import src.test02.Animal as  animal


class Person(animal.Animal):
    a = 1
    s = 'world'
    #  私有变量__XXX
    __d = "wy"

    #  系统定义名字 __XXX__

    #  构造函数有固定的名称 __init__
    def __init__(self, name, age, password, color):
        self.name = name
        self.age = age
        self.__password = password
        self._color = color

    #  析构函数 默认名称__del__ 通常在析构函数中释放类所占的资源
    def __del__(self):
        print("bye bye")

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def say_hello(self):
        print('hello' + self.name)

    def __private_1(self):
        print("private1")

    def __private_2(self):
        print('private2')

    def pub_pri(self, a):
        if a > 1:
            self.__private_2()
        else:
            self.__private_1()


person = Person("nini", 12, 123456, 'red')
person.pub_pri(2)
person.say_hello()
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
# 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
print(person._color)
# 表面上看，外部代码“成功”地设置了__password变量，但实际上这个__password变量和class内部的__password变量不是一个变量！
# 内部的__password变量已经被Python解释器自动改成了_Person__password(不同版本的Python解释器可能会把__password改成不同的变量名)，
# 而外部代码给bart新增了一个__password变量
person.__password = "1234"
print(person.get_password())
print(person.__password)  # 不是class的password，是person这个实例的password
#  使用del删除对象，释放它所占的资源，即调用对象的析构函数
del person
print(animal.Animal.age)
print(animal.Dog.roar("blank"))
