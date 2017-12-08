
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
        total+=list[i]
    print('=', total)
    list[0] =100


list = [1,3,34,45]
sum(list)
print("list:", list)


def print_map(map):
    for(k, v) in map.items():
        print("map[%s]=" % k, v)
    map['name'] = 'tim'


map ={'name': 'johney', 'age': 12}
print_map(map)
print(map)


#  给参数默认值，传参时可以不传有默认值的参数 注：有默认值的参数必须跟在没有默认值的参数后面
def say(messge, times = 1):
    print(messge*times)


say("你好")
say("你好", 3)


#  *开头表示可变长参数是一个元组
def sum2(*t):
    total = 0
    print("t的type：", type(t))
    for x in range(len(t)):
        print(str(t[x])+"+")
        total += t[x]
    print(total)
    return total


print("return sum2:", sum2(1, 3, 5))
#  不给参数即元组为空，输出0
sum2()
#  **开头表示可变长参数为字典


def print_map2(**t):
    for (k, v) in t.items():
        print('t[%s]' % k, v)


print_map2(name='tim', age=12)