import types


def fn():
    pass


# type()
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
# isinstance()
print(isinstance([], (tuple, list)))
print(isinstance((), (tuple, list)))
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('abc'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print(len('abc') == 'abc'.__len__())


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class LenTest:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        return 100

    def printA(self):
        print("AA")


len_test = LenTest('lili')
print(len(len_test))
print(hasattr(len_test, 'name'))  # 有属性'name'吗？
print(hasattr(len_test, 'age'))  # 有属性'age'吗？
setattr(len_test, 'age', 10)  # 设置一个属性'age'
print(hasattr(len_test, 'age'))
print(getattr(len_test, 'age'))  # 获取属性'age'
print(len_test.age)

print(hasattr(LenTest, 'age'))  # 可见设置的age属性，只是在实例上，并不是类
# 也可以获得对象的方法：
print(hasattr(LenTest, "printA"))  # 有属性'printA'吗？
printA = getattr(len_test, "printA")
printA()