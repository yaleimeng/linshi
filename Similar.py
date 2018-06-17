# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/6/17, at 下午 02:04 by PyCharm '''
from pyhanlp import *

Q1 = '申报政府补助的项目还能申报加计扣除吗？'
Q2 = '哪些项目需要市科技局做研发项目的鉴定呢？'


# 获取关键词语序列。
def words_of(Question):
    CRFSegment = JClass("com.hankcs.hanlp.seg.CRF.CRFSegment")
    seg = CRFSegment().enableCustomDictionary(True).seg(Question)
    words =[]
    for term in seg:
        words.append(term.word)  # 则单词归入对应的列表
    return words


def key_words_of(Question):
    '''输入一个原始句子，采用CRF分词方式，然后筛选名词、动词、形容词作为关键词，返回其词表。
    通过词性来筛选关键词只是一种粗略的方法！！！
    '''
    key_words = []
    CRFSegment = JClass("com.hankcs.hanlp.seg.CRF.CRFSegment")
    seg = CRFSegment().enableCustomDictionary(True).seg(Question)

    realist = ['n', 'v', 'a','m', 'q', 'r']
    for term in seg:
        for ele in realist:
            if '{}'.format(term.nature).startswith(ele):  # 如果词性以某个字母开头
                key_words.append(term.word)  # 则单词归入对应的列表
    # 需要对关键词列表去除重复条目。
    return sorted(set(key_words),key=key_words.index)


# 公共词串
def shared_words(Q1, Q2):
    '''给出两个词列表，得出公共词语序列。'''
    common = []
    for word in Q1:
        if word in Q2:
            common.append(word)
    print(common)
    return common


# 词形相似度计算【70%】
def shape_Sim(Q1, Q2):
    len_same = len(shared_words(Q1, Q2))
    return 2.0 * len_same / (len(Q1) + len(Q2))


# 词序相似度 【10%】
def order_Sim(Q1, Q2):
    if not shared_words(Q1, Q2):  # 如果没有公共关键词，取0
        return 0
    if len(shared_words(Q1, Q2)) == 1:  # 如果只有1个公共关键词，取1
        return 1
    else:
        common = shared_words(Q1, Q2)
        position = [Q2.index(word) for word in common]   # 这里简单地取了第一次出现的索引！！！
        inverse = 0
        for ind in range(1, len(position)):
            if position[ind - 1] > position[ind]:
                inverse += 1
        return 1- inverse /(len(common)-1)  # 返回两两比较出现逆序的个数。意味着交换inverse次可以变为升序排列


# 句长相似度。【10%】问题在于，这里的词表，选所有词，还是只选关键词？
def length_Sim(Q1, Q2):
    differ = (len(Q1) - len(Q2)) / (len(Q1) + len(Q2))
    return 1 - abs(differ)



shape = shape_Sim(key_words_of(Q1),key_words_of(Q2))
print('词形相似度为',shape)

length = length_Sim(words_of(Q1),words_of(Q2))
print('句长相似度为',length)

order = order_Sim(key_words_of(Q1),key_words_of(Q2))
print('词序相似度为',order)
