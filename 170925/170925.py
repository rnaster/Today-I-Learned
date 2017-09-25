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
with open('../연구실목록.txt', 'r') as f:
    html = f.read()
parser.feed(html)
# for key, value in parser.dict.items():
#     print(key, value)
