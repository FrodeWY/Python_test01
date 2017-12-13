import subprocess


def subprocess01():
    print('$nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.baidu.com'])
    print('exit code :', r)


# 如果子进程还需要输入，则可以通过communicate()方法输入：
def subprocess02():
    print("$nslookup")
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate(b'set qt=mx\npython.org\nexit\n')
    print(out.decode('gbk'))
    print('exit code :', p.returncode)


if __name__ == '__main__':
    # subprocess01()
    subprocess02()
