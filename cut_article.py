import jieba
import pandas as pd
import pickle

def store_state(file_name, list):
    fileObject = open(file_name, 'wb')
    pickle.dump(list, fileObject)
    print('stored .. ')
    fileObject.close()


def cut_sen(article):
    seg_list = jieba.cut(article, cut_all=False, HMM=True)
    return ' '.join(seg_list)


def get_cutted_article(dataset):
    cutted_articles = []
    for item in dataset:
        cut_article = cut_sen(item)
        cutted_articles.append(cut_article)
    return cutted_articles


news = pd.read_csv("news.csv")
contents = news[~news['content'].isnull()]
article_list = get_cutted_article(contents['content'])
store_state('cutted_article', article_list)