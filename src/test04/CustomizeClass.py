class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'student name:' + self.name


s = Student('wy')
print(s)


class Fib:
    def __init__(self):
        self.a, self.b = 1, 1

    # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
    # 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
    def __iter__(self):
        return self

    def __next__(self):
        if self.a > 10000:
            raise StopIteration()
        self.a, self.b = self.b, self.a + self.b
        return self.a

    # 表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, item):
        a, b = 1, 1
        if isinstance(item, int):
            for i in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            if start is None:
                start = 0
            stop = item.stop
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
    def __getattr__(self, item):
        if item == 'age':
            return 99
        if item == 'score':
            return lambda: 25
        raise AttributeError('student has no attribute %s' % item)


f = Fib()
# for i in Fib():
#     print(i)
print(f[2])
print(f[:5])
print(f.age)
print(f.score)
print(f.score())


# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# print(f.ss)


class Chain:
    def __init__(self, path='api'):
        self._path = path

    def __getattr__(self, item):
        return Chain("%s/%s" % (self._path, item))

    def __str__(self):
        return self._path


print(Chain().status.user.list)


class Student2:
    def __init__(self, name):
        self.name = name

    def print2(self):
        print("print2")

    def __call__(self, *args, **kwargs):
        print("my name is %s" % self.name)


Student2.print2(Student2('sd'))  # 等同实例变量调用,直接使用类调用要传一个实例
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例
s = Student2("lili")
s()

# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student2('ss')))
print(callable(Student('ss')))
print(callable(max))
