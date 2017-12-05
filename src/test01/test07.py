s1 = set([1, 3, 4, 5])
s2 = set([3, 5, 9])
if s1 == s2:
    print('s=s2')
if s1 < s2:
    print('s 是s2的真子集')
elif s1 <= s2:
    print('s是s2的子集')
elif s1 > s2:
    print('s是s2的真超集')
elif s1 >= s2:
    print('s是s2的超集')
s = s1 | s2
print("s,s2并集", s)
print('s,s2并集', s1.union(s))
s = s1 & s2
print('s,s2并集', s)
print('s,s2并集', s1.intersection(s2))
s = s1 - s2
print('s,s2差集', s)
print('s,s2差集', s1.difference(s2))
s = s1 ^ s2
print('s,s2对称差分', s)
print('s,s2对称差分', s1.symmetric_difference(s2))
