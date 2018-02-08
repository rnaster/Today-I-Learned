from nltk.corpus import movie_reviews, stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re
import pandas as pd

class TF_IDF:
    review = movie_reviews.fileids()
    def __init__(self, category):
        self.cate = category
        self.index = 0 if self.cate == 'neg' else 1000
        self.stopword = set(stopwords.words('english'))
    def _load_file(self, filename):
        self.txt = list(movie_reviews.words(fileids=filename))
    def eliminating(self):
        pat = re.compile(r'[a-zA-Z]+', re.I)
        self.txt = list(filter(pat.match, self.txt))
        self.txt = list(filter(lambda x: x not in self.stopword, self.txt))
    def lammatizing(self, pos):
        lemmatizer = WordNetLemmatizer()
        self.txt = list(map(lambda x: lemmatizer.lemmatize(x, pos=pos), self.txt))
    def load_file(self, filename, pos):
        self._load_file(filename); self.eliminating(); self.lammatizing(pos=pos)
        return self.txt
    def FreqDist(self, pos='n'):
        idx = self.index
        self.df = nltk.ConditionalFreqDist((docu, word)
                                           for docu in self.review[idx:idx+1000]
                                           for word in self.load_file(docu, pos))
        self.df = pd.DataFrame(self.df).fillna(0)
        self.df.loc['sum'] = self.df.apply(func=sum, axis=0).values
        self.df = self.df[self.df.applymap(func=lambda x: x < 2).sum(axis=1) != 1000]
        self.df['TF_IDF'] = self.df.apply(func=lambda x: sum(x/self.df.loc['sum']/sum(x != 0)), axis=1)
        self.top15 = self.df.sort_values('TF_IDF', ascending=False)['TF_IDF'].iloc[1:16]
        del self.df

neg = TF_IDF('neg')
pos = TF_IDF('pos')
neg.FreqDist()
pos.FreqDist()
print(neg.top15,'\n','='*30)
print(pos.top15)

