# 递归，递归调用的次数过多，会导致栈溢出
def fact(n):
    if n == 1:
        return 1
    return n + fact(n - 1)


def fact2(n, results):
    if n == 1:
        return results
    return fact2(n - 1, n + results)


# result = fact(998)
# print(result)

# result2 = fact2(998, 1)
# print(result2)


