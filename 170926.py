from nltk.corpus import movie_reviews, stopwords
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd
class TF_IDF:
    review = movie_reviews.fileids()
    def __init__(self, category):
        self.cate = category
        self.index = 0 if self.cate == 'neg' else 1000
        self.df = pd.DataFrame(columns=['word'] + [i for i in range(self.index, self.index+1000)] + ['TF_IDF']).set_index('word')
        self.df.loc['sum'] = [0 for _ in range(1001)]
        self.stopword = set(stopwords.words('english'))
    def load_file(self, filename):
        self.txt = list(movie_reviews.words(fileids=filename))
    def eliminating(self):
        pat = re.compile(r'[\w]+', re.I)
        self.txt = list(filter(pat.match, self.txt))
        self.txt = list(filter(lambda x: x not in self.stopword, self.txt))
    def lammatizing(self, pos='v'):
        lemmatizer = WordNetLemmatizer()
        self.lamma_txt = list(map(lambda x: lemmatizer.lemmatize(x, pos=pos), self.txt))
    def Add(self, idx):
        for word in self.lamma_txt:
            if word not in self.df.index:
                self.df.loc[word, idx] = 1
            else:
                self.df.loc[word, idx] += 1
        self.df.loc['sum', idx] = len(self.lamma_txt)
    def build(self):
        index = self.index
        for idx in range(index, index+1000):
            self.load_file(self.review[idx])
            self.eliminating()
            self.lammatizing()
            self.Add(idx)
            # print(idx)
#     def evaluate(self):
#         for i in