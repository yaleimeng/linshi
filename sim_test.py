# -*- coding: utf-8 -*-
'''
@author: Yalei Meng
@contact: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.

@DateTime: Created on 2018/7/25，at 21:05 by PyCharm
@desc:
'''

from scipy import stats
from gensim.models import Word2Vec, KeyedVectors


# model = Word2Vec.load('C:/wiki.zh.text.model')
model = Word2Vec.load('C:\/wiki_zh_word2vec/wiki0710.model')
# model = Word2Vec.load('D:/opencv/wiki_zh_7.model')
# model = KeyedVectors.load_word2vec_format('D:/cw2vec-0718-final.txt')
test_file = 'wordsim-240.txt'
ideal, real = [], []

with open(test_file, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        w1, w2, score = tuple(line.split())
        try:
            sim = model.similarity(w1, w2)
            real.append(sim)
            ideal.append(float(score))
        except:
            print('发生异常，跳过',line)

# 计算斯皮尔曼系数
print('人工判定：',ideal)
print('计算结果：',real)
relation = stats.spearmanr(ideal, real)[0]
print('当前词向量在'+test_file+'上的斯皮尔曼系数为：',relation)
