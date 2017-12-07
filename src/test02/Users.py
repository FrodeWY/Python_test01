class Users:
    money = 0

    def __init__(self):
        self.money += 1
        self.name = 'lili'

    def __del__(self):
        self.money -= 1

#  静态方法：无法访问实例变量，也不能直接访问静态变量，可以通过类名引用静态变量，因为静态方法既无法访问实例变量又无法直接访问静态变量，
#  所以惊天方法与定义的类没有直接关系，而是起到类似函数工具库的作用
    @staticmethod
    def my_static_method():
        Users.money += 1
        return Users.money

#  类方法和静态方法一样可以使用类名调用，也无法访问实例变量，但可以访问静态变量，类方法需要传代表本类的cls参数
    @classmethod
    def my_class_method(cls):
        print('类：'+str(cls)+'，val:', cls.money, '无法访问name')

#  任何一个公有变量都可以作为静态变量使用，虽然同一个变量通过类名访问和通过对象名访问的实例不同，而且互不干扰
user = Users()
user.money += 1
print(user.money)
print(Users.money)
Users.money += 1
#  静态方法通过类名调用和通过对象名调用没什么区别
print(Users.money)
print(user.name)
print(Users.my_static_method())
print(user.my_static_method())

Users.my_class_method()

#  判断给定的对象是否属于（继承）某个类或类型
print(isinstance(user, Users))