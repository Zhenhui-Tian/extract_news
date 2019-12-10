# coding=utf-8
from ORM import connect_database
import jieba
from gensim.models import word2vec
import data_preprocess
import pandas as pd

# data = connect_database()
# print('read data...')
# #  save same data
data = pd.read_csv('news.csv')

stop_words_path = '/home/terrence/Documents/NLP/NLP_Program/data/stopwords-master/哈工大停用词表.txt'
text = data_preprocess.data_strip_stopword(data['content'].astype(str).tolist(), stop_words_path)
# train word2vec
# text is a set of sentence which is a list of words
print("find cut words")
print(text[:2])
print("start training ...")
model = word2vec.Word2Vec(text)
speakwords = model.most_similar('说', topn=20)
model.save('wordvecModel')
for word in speakwords:
    print(word)
# 这里用model similar 不就得到说的近义词了吗？ 为什么老师说要用深度优先的搜索方法，我是哪一点没有考虑到
# def get_speakword():
#     '''return verbs of speaking such as 说 认为'''
#     speakwords=[]
#     return speakwords

# def speck_synonym(string, num):
#     '''input a string return num synonym'''






