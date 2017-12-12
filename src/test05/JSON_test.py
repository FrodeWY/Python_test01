import json

d = dict(name='Bob', age=20, score=87)


def to_json():
    json_dumps = json.dumps(d)
    print(json_dumps)  # dumps()方法返回一个str，内容就是标准的JSON
    print(type(json_dumps))


def to_json2():
    # dump()方法可以直接把JSON写入一个file-like Object。
    with open('../resource/json.txt', 'w') as j:
        json.dump(d, j)
    # f = open('../resource/json.txt', 'w')
    # json.dump(d, f)


# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
def unjson():
    with open('../resource/json.txt', encoding='utf-8') as r:
        load = json.load(r)
        print('load:', load)
        print('name:'+load['name'])


def unjson2():
    jsons = '{"name": "Bob", "age": 20, "score": 87}';
    loads = json.loads(jsons, encoding='utf-8')
    print("loads:", loads)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


if __name__ == '__main__':
    to_json()
    to_json2()
    unjson()
    unjson2()
    s = Student('Bob', 20, 88)

    # Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
    print(json.dumps(s, default=student2dict))
    # class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
    dumps_json = json.dumps(s.__dict__)
    print(dumps_json)
    print(json.dumps(s, default=lambda obj: obj.__dict__))
    # 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
    # 然后，我们传入的object_hook函数负责把dict转换为Student实例：
    print(json.loads(dumps_json, object_hook=dict2student))
