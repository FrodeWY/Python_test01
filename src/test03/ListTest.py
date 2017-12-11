#  列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
import os

list1 = [x * x for x in range(1, 10)]
print(list1)
#  for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
list2 = [x * x for x in range(1, 100) if x % 2 == 0]
print(list2)
list3 = [m * n for m in range(1, 10) for n in range(1, 10)]
list4 = [m + n for m in 'adc' for n in 'def']
print(list3)
files = [file for file in os.listdir('.')]
print(files)
dict1 = {'color': 'red', 'age': 12}
dicts = [k + '=' + str(v) for k, v in dict1.items()]
print(dicts)
L = ['SAS', 'DWA', 'gaSDS', 12]
lowList = [a.lower() for a in L if isinstance(a, str)]
print(lowList)
