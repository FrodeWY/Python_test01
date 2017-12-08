import math
import random
from decimal import Decimal
from decimal import getcontext
from fractions import Fraction

# math
print(math.e)
print(math.pi)

# random
print(random.random())  # 0-1随机数
print(random.uniform(1, 4))
print(random.uniform(4, 1))
print(random.randint(1, 4))  # 随机整数
print(random.randrange(1, 10, 2))  # 按照指定基数递增的集合中获取一个随机数
t = (1, 4, 2)
l = [1, 42, 65]
print(random.choice(l))  # 从指定序列中获取一个随机元素，参数为有序类型可以是列表，元组，字符串
print(random.choice("fdsfa"))
print(random.sample(l, 2))  # 从指定序列中获取一个指定长度的随机片段
random.shuffle(l)  # 将列表元素打乱
print(l)

# decimal
d = Decimal("1.0")
d2 = Decimal("3.0")
print(d / d2)  # 默认28位
getcontext().prec = 6  # 设置小数点精度
print(d / d2)

# fraction
print(Fraction(2, 4))  # 表示分数1/3，fraction可以自动约分
print(Fraction(1, 6) * 3)
