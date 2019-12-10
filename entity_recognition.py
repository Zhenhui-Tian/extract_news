from pycorenlp import StanfordCoreNLP
from pyltp import NamedEntityRecognizer
import pickle
from pos import store_state
import pandas as pd
#  这个文件的主要作用是找到人名的


file = open(r'C:\Users\Terrence\Documents\NLP\extract_news\temp_data\pos.pickle', 'rb')
pos_pd = pd.DataFrame(pickle.load(file))

ner_model = r'C:\Users\Terrence\Documents\NLP\NLP_tools\ltp_data_v3.4.0\ltp_data_v3.4.0\ner.model'
reg = NamedEntityRecognizer()
reg.load(ner_model)
reg_dict = {'sentence': [], 'tags': [], 'ner': []}
for index, row in pos_pd.iterrows():
    ner = reg.recognize(row['sentence'], row['tags'])
    reg_dict['sentence'].append(row['sentence'])
    reg_dict['tags'].append(row['tags'])
    reg_dict['ner'].append(list(ner))

store_state(r'C:\Users\Terrence\Documents\NLP\NLP_tools\ltp_data_v3.4.0\ltp_data_v3.4.0\ner.pickle', reg_dict)
file = open(r'C:\Users\Terrence\Documents\NLP\NLP_tools\ltp_data_v3.4.0\ltp_data_v3.4.0\ner.pickle', 'rb')

reg.release()


















# 这里是尝试用语法来进行chunk
#
# fileobject = open('coreNlpPos', 'rb')
# articles = pickle.load(fileobject, encoding='utf8')
# # stanford_nlp = StanfordCoreNLP('http://localhost/9000') #我把9000 写到前面的字符串里出错，port要单独写出来
# print("connected ... ")
#
# sentence = articles[0]
# print(sentence)
# grammar = r"""
# NP: {<DT|JJ|NN.*>+}
# PP: {<IN><NP>}
# VP: {<VB.*><NP|PP|CLAUSE>+$}
# CLAUSE: {<NP><VP>}
# """
# cp = nltk.RegexpParser(grammar)
# result = cp.parse(sentence)
# result.draw()

# stanford_nlp.close()

