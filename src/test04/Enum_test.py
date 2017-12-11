from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Jan = Month.Jan
print(type(Jan))
for name, member in Month.__members__.items():
    print('name:', name, '  member:', member, '  member Value:', member.value)


# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


sun = Weekday.Sun
print(sun)
print(sun.value)
print(Weekday['Mon'])
print(Weekday(1))
for name, member in Weekday.__members__.items():
    print('name:', name, '  member:', member, '  member Value:', member.value)



