import src.test02.Animal as  animal


class Person(animal.Animal):
    a = 1
    s = 'world'
#  私有变量__XXX
    __d = "wy"
#  系统定义名字 __XXX__


#  构造函数有固定的名称 __init__
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.__password = password

#  析构函数 默认名称__del__ 通常在析构函数中释放类所占的资源
    def __del__(self):
        print("bye bye")

    def say_hello(self):
        print('hello'+self.name)


person = Person("nini", 12, 123456)
person.say_hello()
#  使用del删除对象，释放它所占的资源，即调用对象的析构函数
del person
print(animal.Animal.age)
print(animal.Dog.roar("blank"))
