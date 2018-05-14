# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/5/14, at 下午 01:27 by PyCharm '''


from pyhanlp import *

wd ={}
no_list = ['u','w','y',]
with open('D:/XMWT.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        seg = HanLP.segment(line.strip())
        for term in seg:
            for ele in no_list:
                if '{}'.format(term.nature).startswith(ele):  # 如果词性无用，直接忽略。
                    break
            else:
                print(term,end=' ')  # 打印该词
        print('')
#
# from collections  import OrderedDict
# realist = ['n','v','a','m','q','r']
# wd = OrderedDict()          # .fromkeys(realist,[])   # 初始化词典的值
# for ele in realist:
#     wd[ele] = []
# for term in seg:
#     for ele in realist:
#         if '{}'.format(term.nature).startswith(ele): # 如果词性以某个字母开头
#             wd[ele].append('{}'.format(term.word))   # 则单词归入对应的列表
#
# for k,v in wd.items():
#     print(k,v)