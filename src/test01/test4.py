menuList = ['红烧肉', '炒肉丝', '宫爆鸡丁']
print(menuList)
print(len(menuList))
print(menuList[1])
menuList.append('北京烤鸭')
print(menuList)
menuList.insert(1, '炒肝')
print(menuList)
menuList2 = ['西红柿炒鸡蛋', '京酱肉丝']
menuList3 = menuList + menuList2
if '京酱肉丝' in menuList2:
    print("有京酱肉丝")
print(menuList3)
menuList.extend(menuList2)
print(menuList)
print(menuList.index('红烧肉'))
menuList.remove('京酱肉丝')
print(menuList)
for i in range(len(menuList)):
    print(menuList[i])

for index, value in enumerate(menuList):
    print(index, value)
numList = [1, 3, 2, 7, 4]
numList.sort()
menuList.sort()
print(numList)
print(menuList)
numList.reverse()
print(numList)
# 默认起始值为0
list1 = range(10)
list2 = range(10, 20)
for index, value in enumerate(list1):
    print(index, value)
list3 = [["cpu", "gpu"], ["硬盘", "声卡"]]
for i in range(len(list3)):
    print(list3[i])
    for j in range(len(list3[i])):
        print(list3[i][j])
#  元组可以储存数字，字符串，甚至是元组，元组不可被改变，所以元组没有sort方法
t = (1, 6, 3, 4)
for i in range(len(t)):
    print(t[i])
#  list() 转列表，tuple（）转元组
list4 = list(t)
list4.sort()
print(list4)
t2 = tuple(list4)
print(t2)