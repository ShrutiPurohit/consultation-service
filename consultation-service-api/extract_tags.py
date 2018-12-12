from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from nltk.tokenize import RegexpTokenizer
import pandas as pd

class ExtractTags(object):
    """docstring for ExtractTags."""
    def __init__(self, lang='english', reg=r'\w+'):
        super(ExtractTags, self).__init__()
        self.stop_words = set(stopwords.words(lang))
        self.lemmatizer = WordNetLemmatizer()
        self.tokenizer = RegexpTokenizer(reg)
        self.tags = self.update_tags()

    def __stemming(self, text):
        return [s for s in text if s not in self.stop_words]

    def __lemmatize(self, s):
        return [self.lemmatizer.lemmatize(w) for w in s]

    def update_tags(self):
        t = pd.read_csv('C:\\Users\\Shruti\\Documents\\Virtual\\design_project\\helper\\tags.csv')
        t.tags = t.tags.str.lower()
        return t.tags.tolist()

    def get_tags(self, text):
        s = text.lower()
        s = self.tokenizer.tokenize(s)
        s = [re.sub(r'[^\w\s]','',i) for i in s]
        s = [i for i in s if len(i)!=0]
        s = self.__stemming(s)
        s = self.__lemmatize(s)
        return list(set([word for word in s if word in self.tags]))


# def main():
#     extract_tags = ExtractTags(lang='english')
#     questions = pd.read_csv('ques.csv')
#     for i in questions.questions:
#         print("\nDescription: ", i, "\n\nTags: ", ', '.join(extract_tags.get_tags(i)))


# if __name__ == '__main__':
#     main()
