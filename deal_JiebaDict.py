# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/8/15, at 下午 02:09 by PyCharm '''

#  jieba.dict.txt
with open('D:/jieba5/Hanyu.txt', 'r', encoding='utf-8') as fd, open(
        'data/how_Def00.txt', 'r', encoding='utf-8') as fmid,open(
        'Different.txt', 'w', encoding='utf-8') as fs:
    jdic,hdic = set(),set()     # 经过集合运算，也就混乱了顺序。省得再自己打乱了。

    for line in fd.readlines():         # 收集结巴词汇表。34.95万
        if line.strip():
            jdic.add(line.strip().split()[0])
    for line in fmid.readlines():       # 读取已收集的知网词汇
        if line.strip():
            hdic.add(line.strip().split()[1])

    useful = list(jdic - hdic)  # 对二者的差集，转换为列表。方便做切片。
    length = len(useful)

    paras = [useful[i:i+120 if i+120<length else length]
             for i in range(0,len(useful),120)]    # 这就是切片的列表。
    for para in paras:
        sentence = ''.join(para)   # 用空格将词汇串联起来！！
        print(sentence)
        fs.write(sentence + '\n')   # 写入到新文件！
    print(len(jdic), len(hdic), '未采集词汇数量：', length)