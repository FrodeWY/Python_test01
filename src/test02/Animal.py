import time


class Animal:
    type = ""
    age = 0

    def __init__(self, type, age, color):
        self.type = type
        self.age = age
        self.color = color

    def dispAnimalType(self):
        print(self.type)

    def roar(self):
        print("animal roar")


class Dog(Animal):
    name = ""

    def __init__(self, name):
        self.name = name
        self.type = "狗"

    def roar(self):
        print('汪...')


# 继承的好处：多态
def test(animal):
    animal.roar()


#  继承
dog = Dog('妮妮')
print(dog.age)
dog.dispAnimalType()
dog.roar()
now = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
print(now)

animal = Animal('animal', 12, 'red')
test(dog)
test(animal)
# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
