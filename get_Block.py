# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/5/14, at 下午 01:27 by PyCharm '''

from pyhanlp import *

useless = []
with open('D:/stopPhrase.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        useless.append(line.strip())

wd = {}
no_list = ['u', 'w', 'y', 'ad', ]
with open('D:/XMWT.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        sentence = line.strip()
        for stop in useless:
            sentence = sentence.replace(stop, '')
        seg = HanLP.segment(sentence)
        for term in seg:
            for ele in no_list:
                if '{}'.format(term.nature).startswith(ele):  # 如果词性无用，直接忽略。
                    break
            else:
                print(term, end=' ')  # 打印该词
        print('')
#
