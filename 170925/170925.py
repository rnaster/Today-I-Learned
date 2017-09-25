from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dict = {'labName': [], 'professor': [], 'location': [], 'phone': [], 'abbreviation': []}
    def handle_starttag(self, tag, attrs):
        if tag == 'br': self.label_ = 'phone'
        if attrs != []:
            self.label_ = ''
            if 'lab' in attrs[0][1]:
                self.label_ = 'labName'
            elif 'professor' in attrs[0][1]:
                self.label_ = 'professor'
            elif 'office' in attrs[0][1]:
                self.label_ = 'location'
            elif 'abbreviation' in attrs[0][1]:
                self.label_ = 'abbreviation'
    def handle_data(self, data):
        data = data.strip()
        if data in ['', ','] or self.label_ == '': return
        self.dict[self.label_].append(data.strip())

parser = MyParser()
with open('연구실목록.txt', 'r') as f:
    html = f.read()
parser.feed(html)
# for key, value in parser.dict.items():
#     print(key, value)

import re
string1 = 'Earth is the third planet from the Sun'
pat = re.compile(r'(\w{2})([\w]+| )', re.I)
result = re.findall(pat, string1)
# for i,_ in result:
#     print(i, end=' ')

string2 = 'abc.test@gmail.com, xyz@test.in, test.first@analyicsvidhya.com, first@rest.biz'
pat = re.compile(r'@[\w.,]+')
# print(re.findall(pat, string2))

string3 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
pat = re.compile(r'\d{2}-\d{2}-\d{4}')
# print(re.findall(pat, string3))

string4 = 'Earth`s gravity interacts with other objects in space, especially the Sun and the Moon.'
# pat = re.compile(r'')