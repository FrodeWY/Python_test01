import datetime
import time


def time01():
    # 获取当前日期和时间
    now = datetime.datetime.now()
    print(now)
    # 获取指定日期和时间
    dt = datetime.datetime(2015, 4, 19, 12, 20)
    print(dt)
    # datetime转换为timestamp 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
    #  当前时间就是相对于epoch time的秒数，称为timestamp。

    # 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
    # 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
    # 这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
    dt_timestamp = dt.timestamp()
    print('dt.timestamp:', dt_timestamp)

    # timestamp转换为datetime
    fromtimestamp = datetime.datetime.fromtimestamp(dt_timestamp)
    # timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。timestamp和本地时间做转换。
    print('fromtimestamp:', fromtimestamp)
    # imestamp也可以直接被转换到UTC标准时区的时间：
    utcfromtimestamp = datetime.datetime.utcfromtimestamp(dt_timestamp)
    print('utcfromtimestamp:', utcfromtimestamp)
    # str转换为datetime
    datetime_str = '2015-6-1 18:19:59.45'
    datetime_str2 = '2015-7-1 18:19:59.45'
    datetime_strptime1 = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
    datetime_strptime2 = datetime.datetime.strptime(datetime_str2, '%Y-%m-%d %H:%M:%S.%f')
    print('datetime_strptime2-datetime_strptime1=', datetime_strptime2 - datetime_strptime1)
    print(datetime_strptime1)
    # datetime转换为str
    datetime_strftime = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S.%f")
    print(datetime_strftime)


# datetime加减
def time02():
    now = datetime.datetime.now()
    t1 = now + datetime.timedelta(hours=10)
    t2 = now - datetime.timedelta(days=1)
    t3 = now + datetime.timedelta(days=1, hours=12)
    print(t1, t2, t3)


# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
def timezone_transform():
    utc_dt = datetime.datetime.utcnow()
    # 指定时区
    utc_dt2 = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    print(utc_dt, '\n', utc_dt2)
    bj_dt = utc_dt2.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    print('北京时间：', bj_dt)
    # now.replace(tzinfo=datetime.timezone.)


# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
def localtime_to_utctime():
    tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now().replace(tzinfo=tz_utc_8)
    now_timestamp = now.timestamp()
    print(now)
    print(now_timestamp)

# 根据时区，和时间获得timestamp
def to_timestamp(dt_str, tz):
    dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tr_dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=tz))).timestamp()
    # bj_dt = datetime.datetime.fromtimestamp(tr_dt).astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    # print(bj_dt)
    print(tr_dt)


if __name__ == '__main__':
    # time02()
    # timezone_transform()
    localtime_to_utctime()
    to_timestamp('2015-6-1 08:10:30', 7)
