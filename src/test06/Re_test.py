import re


# |B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。
# 你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；



def re01():
    regex = r'正则表达式'
    test = '用户输入字符串'
    if re.match(regex, test):
        print('ok')
    else:
        print('failed')


def re02():
    regex = r'^\w{8,16}@[a-zA-z]{2}\.\w{3,4}$'
    if re.match(regex, '841234684@qq.com'):
        print('ok')
    else:
        print('failed')


# 用正则表达式切分字符串比用固定的字符更灵活/s
def re_split():
    regex = r'\s+'
    test = 'a b   c'
    split = re.split(regex, test)
    split2 = str.split(test, ' ')
    print(split, '\n', split2)


def re_split2():
    regex = r'[\s\,\;\.]+'
    test = 'a, b, c;; k.  d'
    split = re.split(regex, test)
    split2 = str.split(test, ' ')
    print(split, '\n', split2)


# 正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）,注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
def re_group():
    regex = r'^(\d{3})-(\d{0,9})$'
    test = '010-12345'
    match = re.match(regex, test)
    print(match)
    print(match.groups())
    print(match.group(0))


# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符,由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
def re_greedy():
    regex = r'^(\d+)(0*)$'
    test = '012340000'
    match = re.match(regex, test)
    print(match.groups())


# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
def re_greedy2():
    regex = r'^(\d+?)(0*)$'
    test = '012340000'
    match = re.match(regex, test)
    print(match.groups())





# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
re_compile = re.compile(r'^(\d{3})-(\d{3,8})$')
def re_compile_method():
    match = re_compile.match('010-1254')
    if match:
        print('ok')
        print(match.groups())
    else:
        print('failed')


if __name__ == '__main__':
    # re01()
    # re02()
    # re_split()
    # re_split2()
    # re_group()
    # re_greedy()
    # re_greedy2()
    re_compile_method()
