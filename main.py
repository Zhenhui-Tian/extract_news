# -*- coding: utf-8 -*-
from pyltp import Segmentor
import pandas as pd
import pickle
import re


def store_state(file_name, store_list):
    fileObject = open(file_name, 'wb')
    pickle.dump(store_list, fileObject)
    print('stored .. ')
    fileObject.close()


# read data and process
news = pd.read_csv(r'C:\Users\Terrence\Documents\NLP\temp_data\news.csv')
clean_news = news[~news['content'].isnull()]
clean_content = clean_news['content']
articles = [item for item in clean_content]
articles = [re.split('。|\n|;', sen) for sen in articles]
print(articles[0])

# 分词

ldir = r'C:\Users\Terrence\Documents\NLP\NLP_tools\ltp_data_v3.4.0\ltp_data_v3.4.0\cws.model'
segmentor = Segmentor()
segmentor.load(ldir)
cutted_sentence = []
i = 0
for article in articles:
    print('{} article processing\r'.format(i))
    i += 1
    for sen in article:
        words = segmentor.segment(sen)
        # words 是一个list的接口
        cutted_sentence.append(list(words))

store_state(r'C:\Users\Terrence\Documents\NLP\temp_data\words.pickle', cutted_sentence)
segmentor.release()

