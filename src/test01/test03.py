import datetime
a = 15
b = 7
if a > 10:
    print("a>10")
    if a > 14:
        print("a>14")
if b > 10:
    print("b>10")
elif b > 8:
    print("b>8")
else:
    print("b<8")

c = "今天是"
d = datetime.datetime.now()
e = d.weekday()
print(e)
if e == 0:
    c += "星期一"
elif e == 1:
    c += "星期二"
elif e == 2:
    c += "星期三"
elif e == 3:
    c += "星期四"
elif e == 4:
    c += "星期五"
elif e == 5:
    c += "星期六"
elif e == 6:
    c += "星期天"
print(c)
f = 1
sum = 0
while f < 10:
    print("f:",f)
    sum += f
    f += 1
print(sum)

g = 1
sum2 = 0
for g in range(1, 100):
    if g == 50:
        break
    if g % 2 != 0:
        continue
    print("g:", g)
    sum2 += g
print(sum2)

try:
    h = 10
    print(30/(10 - h))
except Exception as e:
    print(e)
finally:
    print("end")
