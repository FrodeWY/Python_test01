def print_welcome(str1, str2):
    print(str1, str2)


print_welcome("hello ", "world")


#  形参不会改变实参,但是如果参数是列表,字典形参改变会影响实参
def func(num):
    print('a的形参地址', id(num))
    num += 1


a = 1
func(a)
print('a的实参地址', id(a))
print(a)


def sum(list):
    total = 0
    for i in range(len(list)):
        print(list[i], "+")
        total += list[i]
    print('=', total)
    list[0] = 100


list = [1, 3, 34, 45]
sum(list)
print("list:", list)


def print_map(map):
    for (k, v) in map.items():
        print("map[%s]=" % k, v)
    map['name'] = 'tim'


map = {'name': 'johney', 'age': 12}
print_map(map)
print(map)


#  给参数默认值，传参时可以不传有默认值的参数 注：有默认值的参数必须跟在没有默认值的参数后面,定义默认参数要牢记一点：默认参数必须指向不变对象！
#  Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#  如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#  不能指向list,set ,map否则值会追加,解决方法l=None
def say(messge, times=1, l=[]):
    l.append('end')
    print(l)
    print(messge * times)


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


say("你好")
say("你好", 3)
i = calc((1, 3))
print(i)


#  *开头表示可变长参数是一个元组,调用该函数时，可以传入任意个参数，包括0个参数：
#  如果已经有一个list或者tuple，要调用一个可变参数,在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
def sum2(*t):
    total = 0
    print("t的type：", type(t))
    for x in range(len(t)):
        print(str(t[x]) + "+")
        total += t[x]
    print(total)
    return total


print("return sum2:", sum2(1, 3, 5))
#  不给参数即元组为空，输出0
print("return sum2:", sum2())
lists = [2, 4]
sum2(*lists)


#  关键字参数:**开头表示可变长参数为字典
#  如果已经有dict，要调用一个关键字参数,dict前面加一个*号，dict的元素变成可变参数传进去：
def print_map2(**t):
    for (k, v) in t.items():
        print('t[%s]' % k, v)


#  如果要限制关键字参数的名字，就可以用命名关键字参数,命名关键字参数需要一个特殊分隔符*
def print_map3(name, *, city, age):
    print(name, city, age)


#  如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def print_map4(name, *age, city, color):
    print(name, city, age, color)


print_map2(name='tim', age=12)
print_map2()
print_map3('lili', city='beijing', age=12)
print_map4('lili', 1, 2, 3, city='nanjing', color='red')
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
