# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))
print(g)
print(next(g))
for n in g:
    print(n)

# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 自定义生成器：函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。
# 斐波拉契数列:
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        n += 1
        # print(b)
        yield b
        a, b = b, a + b
    return 'done'


f = fib(5)
print(next(f))
# 这样拿不到return的值，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
# for a in f:
#     print(a)
print('--------------------')
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
