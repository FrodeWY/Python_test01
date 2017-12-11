from types import MethodType


# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student:
    pass


s = Student()
# 然后，尝试给实例绑定一个属性：
s.name = "lili"


def set_age(self, age):
    self.age = age


# 还可以尝试给实例绑定一个方法：
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(9)
print(s.age)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
print(hasattr(s2, "set_age"))
print(hasattr(s, 'set_age'))
# 为了给所有实例都绑定方法，可以给class绑定方法：
# MethodType(set_age, Student)给Student 创建一个方法 但这里不是在class中创建而是创建了一个链接把外部的set_age 方法用链接指到Student内
# Student.set_age = MethodType(set_age, Student)


Student.set_age = set_age
s3 = Student()
s4 = Student()
s3.set_age(20)
s4.set_age(30)  # 如果使用 MethodType(set_age, Student)第二个会覆盖第一个
print(s3.age, s4.age)
print(hasattr(s3, 'set_age'))


# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student2:
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

st1 = Student2()
st1.name = 'titi'
st1.age = 12


# st1.score = 100


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student2):
    pass


gs = GraduateStudent()
gs.name = 'qiqi'
gs.score = 13
print(gs.score)


# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class GraduateStudent2(Student2):
    __slots__ = ('score')
    pass


gs2 = GraduateStudent2()
gs2.name = 'ww'
gs2.age = 15
gs2.score = 100
# gs2.color = "red"
