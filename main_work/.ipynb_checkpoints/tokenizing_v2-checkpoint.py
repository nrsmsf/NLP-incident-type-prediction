import re, nltk, sys, spacy
from names import *
from mylist import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = [stopwords.words('russian') + mylist1 + names1]




def lemmatize_ru(text):
    nlp = spacy.load('ru_core_news_sm', disable=['parser', 'ner'])
    doc = nlp(text)

    tokenized_and_lemmatized = ([token.lemma_ for token in doc])

    return tokenized_and_lemmatized



def cleaning_ru(texts, stop_words=stop_words):

    filtered1 = ' '.join(texts).split()
    filtered_string = ' '.join(filtered1)

    cleaned2 = re.sub('\d+', '', filtered_string)
    cleaned3 = re.sub(r'http\S+', '', cleaned2)
    #cleaned1 = re.sub('(\w+(in|ov|va|uk|ko|ky)\w*)', '', cleaned3)
    x1 = re.sub('\W+', ' ', cleaned3.lower())

    tokenized = x1.split(" ")

    filtered = [word for word in tokenized if word not in stop_words[0]]
    filtered1 = ' '.join(filtered).split()
    filtered_string = ' '.join(filtered1)
    return filtered_string
    