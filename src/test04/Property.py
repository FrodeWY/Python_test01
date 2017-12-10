# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
# 但是，这种调用方法又略显复杂，没有直接用属性这么直接简单。有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter
# 负责把一个setter方法变成属性赋值
class Student:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('age must be int')
        if age > 100 or age < 0:
            raise ValueError('age must between  0-100')
        self._age = age

    # 只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def age2(self):
        return 100 - self._age


s = Student()
# s.score=101
s.age = 10
print(s.age)
print(s.age2)
s.age2 = 100  # 而age2就是一个只读属性
