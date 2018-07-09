#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 使用gensim word2vec训练脚本获取词向量

import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告

import logging
import os.path
import sys

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def retrain(data_file, old_model_file, new_model):  # 增量训练功能。
    sents = LineSentence(data_file)             # 用数据文件创建单行句子对象。
    model = Word2Vec.load(old_model_file)  # 用原模型文件构造模型
    model.build_vocab(sents, update=True)
    model.train(sents, total_examples=model.corpus_count, epochs=model.iter)
    model.save(new_model + '.model')  # 保存为新文件
    model.wv.save_word2vec_format(new_model + '.vector', binary=False)


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inp为输入语料, outp1 为输出模型, outp2为原始c版本word2vec的vector格式的模型
    fdir = './'
    inp = fdir + 'wiki_zh_seg.txt'
    outp1 = fdir + 'wiki.zh.text.model'
    outp2 = fdir + 'wiki.zh.text.vector'

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inp), size=300,  # 词向量维度：越大效果越好，但需要语料更多。当前合理值在200左右
                     window=10,  # 表示当前词与预测词在一个句子中的最大距离是多少
                     min_count=10,  # 词频少于min_count次数的单词，认为是没有意义的，会被丢弃。一般的取值5或者10
                     sg=1,  # 设置训练算法，默认为0，对应CBOW算法；sg=1则采用skip-gram算法。后者更好，但慢两倍。
                     hs=0,  # 如果hs为1，则会采用hierarchical softmax技巧。如果为0（默认），则negative sampling会被使用。
                     negative=20,  # 如果>0，则会采用negative sampling，用于设置多少个noise words。一般取5——20
                     iter=5,  # 迭代次数，默认为5次。
                     workers=4  # 工作线程数。
                     )
    # 保存模型
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)
