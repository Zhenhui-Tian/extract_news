import jieba
import pandas as pd
import re

# 这里 训练词向量的预处理和pos的预处理不一样 pos的预处理直接借助pltpy就可以了从分句到分词
def data_strip_null(file, column):
    '''input is pandas dataframe,
    column is the column which will be check if there are none value if so, delete this row
    '''
    return file[~file[column].isnull()]


def article_to_clean_sentences(article):
    article = re.sub('([。！？？])([^’“])', r"\n", article)
    article = re.sub('(\.{6})([^’“])', r"\n", article)
    article = re.sub('((\.\.\.){2})([^’“])', r"\n", article)
    article = re.sub('([。！？？][’“])([^。！？？])', r"\n", article)
    article = re.sub('[n\u3000]|[\u3000]|[\\\\n]|[\r]]', r"\n", article)
    article = article.rstrip()
    sentences = article.split('\n')
    return sentences


# 例子都是cut句子 所以我们是不是要先转化成句子再cut
def data_strip_stopword(content, stop_words_path):
    # 将文字全部转化成简体

    # 读取哈工大中文stop, words
    stop_words = [line.strip() for line in open(stop_words_path, encoding='utf8').readlines()]
    # tokenize

    content_list = []
    # 这里一个item应该是一篇文章
    for item in content:
        sens = article_to_clean_sentences(item)
        for sen in sens:
            if sen != "":
                seg_list = jieba.cut(sen)
                content_list.append(" ".join(seg_list))
    # 注意这里的split，这样原来的content 是一整个string
    print(content_list[0])
    articles = []
    for item in content_list:
        sent = item.split(" ")
        clean_sent = []
        for word in sent:
            if word not in stop_words:
                clean_sent.append(word)
        articles.append(clean_sent)
    return articles


# # test part
# data = pd.read_csv('news.csv')
# content = data['content'].astype(str)
# stopword_path = '/home/terrence/Documents/NLP/NLP_Program/data/stopwords-master/哈工大停用词表.txt'
# # content = content.tolist()
# text = data_strip_stopword(content.tolist(), stopword_path)
# print(text)
