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


class Dog(Animal):
    name = ""

    def __init__(self, name):
        self.name = name
        self.type = "狗"

    def roar(self):
        print('汪...')

#  继承
dog = Dog('妮妮')
print(dog.age)
dog.dispAnimalType()
dog.roar()
now = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
print(now)