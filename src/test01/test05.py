m1 = {'name': '小明', 'age': 13, 'score': 95}
print(m1)
print(m1["name"])
print(len(m1))
m1['sex'] = '男'
print(m1)
m2 = {'color': 'red', 'price': 12.423}
m1.update(m2)
print(m1)
m1.pop("price")
print(m1)
if 'price' in m1:
    print(m1['price'])
else:
    print('不含price')
for key in m1.keys():
    print('键:'+key+' 值：', m1[key])
for value in m1.values():
    print(value)
m1.clear()
print(m1)
m2 = {'name': {'first': 'Johney', 'last': 'Lee'}, 'age': 13}
print(m2['name']['first'])