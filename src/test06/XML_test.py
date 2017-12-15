from encodings.utf_8 import encode
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler():
    def start_element(self, name, attr):
        print("sax:start_element:%s,attr:%s" % (name, attr))

    def end_element(self, name):
        print("sax:end_element:%s" % name)

    def char_data(self, text):
        print('sax:char_data:%s' % text)


def sax_handler():
    parser_create = ParserCreate()
    handler = DefaultSaxHandler()
    parser_create.StartElementHandler = handler.start_element
    parser_create.EndElementHandler = handler.end_element
    parser_create.CharacterDataHandler = handler.char_data
    xml = r'''<?xml version="1.0"?>
    <ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''
    print(parser_create.Parse(xml))


# def create_xml():
#     L = []
#     L.append(r'<?xml version="1.0"?>')
#     L.append(r'<root>')
#     L.append(encode('some & data'))
#     L.append(r'</root>')
#     return ' '.join(L)

if __name__ == '__main__':
    # s = create_xml()
    # print(s)
    sax_handler()
