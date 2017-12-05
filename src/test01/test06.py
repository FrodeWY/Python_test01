#  无序可变集合,集合元素唯一不重复
s = set('python')
s2 = set('hello')
print(type(s))
print(s)
s2.update(s)
print(s2)
#  添加元素
s.add('l')
print(s)
s.remove('p')
print(s)
#  随机弹出
print(s.pop())
print(s)
for e in s:
    print(e)
if 'y' in s:
    print('s集合有 y')
s.clear()
print(s)


#  无序不可变集合，集合元素唯一不重复
fs = frozenset('python')
print(type(fs))
print(fs)
print(len(fs))


s3 = set([1, 2, 4])
print(s3)

