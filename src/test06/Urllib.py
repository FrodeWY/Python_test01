from urllib import request, parse


# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
def urlopen01():
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print('Data:', data.decode('utf-8'))


# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页
# 这样豆瓣会返回适合iPhone的移动版网页：
def request_urllib():
    req = request.Request('http://www.douban.com/')
    # req.add_header('User-Agent',
    #                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        data = f.read()
        for k, v in f:
            print('%s:%s' % (k, v))
        print('Data:', data.decode('utf-8'))


# urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
def post_urllib():
    print('Login to weibo.cn...')
    # python input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。
    email = input('Email: ')
    passwd = input('Password: ')
    # urlencode这个方法可以将字典转换为url参数
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    print(login_data)
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
def handler():
    proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        data = f.read()
        print(data.decode('utf-8'))


if __name__ == '__main__':
    # urlopen01()
    # request_urllib()
    post_urllib()
    # handler()
