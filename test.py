# coding=utf-8
import sys
from gensim.models import Word2Vec
model = Word2Vec.load("/home/terrence/Documents/NLP/NLP_Program/extract_idea/wordvecModel")
words = model.most_similar('认为', topn=20)
print(words)