import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    # print(addr)
    # print(Header(name, 'utf-8').encode())
    # print(formataddr((Header(name, 'utf-8').encode(), addr)))
    return formataddr((Header(name, 'utf-8').encode(), addr))


def SMTP01():
    # 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    # 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
    # msg = MIMEText('hello,send by python..', 'plain', 'utf-8')
    msg = MIMEText(
        '<html><body><h1>Hello</h1><p>send by<a href="http://www.python.org"> python</a>..</p></body></html>',
        'html', 'utf-8')

    from_addr = 'wy841234684@sohu.com'
    password = 'q13073150747'
    to_addr = 'wy841234684@163.com'
    smtp_server = 'smtp.sohu.com'
    #邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
    # 而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中
    msg['From'] = _format_addr('python爱好者<%s>' % from_addr)
    msg['To'] = _format_addr('管理员<%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候。。。。', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    # 来登录SMTP服务器
    server.login(from_addr, password)
    # 打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# 发送附件:可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象
def SMTP02():
    #  邮件对象:
    msg = MIMEMultipart()
    from_addr = 'wy841234684@sohu.com'
    password = 'q13073150747'
    to_addr = 'wy841234684@163.com'
    smtp_server = 'smtp.sohu.com'
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    # 邮件正文是MIMEText
    msg.attach(
        MIMEText('<html><body><h1>Hello</h1><p>send by<a href="http://www.python.org"> python</a>..</p></body></html>',
                 'html', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('../resource/cat.jpg', 'rb') as  f:
        # 设置附件的MIME和文件名，这里是jpg类型:
        mime = MIMEBase('image', 'jpg', filename='cat.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition','attachment',filename='test.jpg')
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-Id','0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    server = smtplib.SMTP(smtp_server,25)
    server.login(from_addr,password)
    server.set_debuglevel(1)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.close()





if __name__ == '__main__':
    # SMTP01()
    SMTP02()
