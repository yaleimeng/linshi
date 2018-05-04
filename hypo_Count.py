# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/5/4, at 下午 02:15 by PyCharm '''

import  collections

head = set()
mydict = collections.OrderedDict()
with open('cilin.txt', 'r', encoding='gbk') as f:
    # 第一次遍历，得到大中小类的代码。
    for line in f.readlines():
        res = line.split()
        code = res[0]  # 词义编码
        if len(code)<6:
            continue
        fathers = [code[:1],code[:2],code[:4],code[:5]]
        head.update(fathers)
    fatherlist = sorted(list(head))


with open('cilin.txt', 'r', encoding='gbk') as f:
    # 第二次遍历：得到大中小类的数量。
    for ele in fatherlist:
        mydict[ele] = 0
    for line in f.readlines():
        res = line.split()
        code = res[0]  # 词义编码
        words = res[1:]  # 同组的多个词
        if len(code)>5 and  code[:5] in mydict.keys():
            mydict[code[:5]] += len(words)
        if len(code)>4 and  code[:4] in mydict.keys():
            mydict[code[:4]] += len(words)
        if len(code)>2 and code[:2] in mydict.keys():
            mydict[code[:2]] += len(words)
        if len(code)>1 and code[:1] in mydict.keys():
            mydict[code[:1]] +=len(words)


import math
FenMu = 16.5858281163

def Info_Content(concept):
    hypo=1
    if concept in mydict.keys():
        hypo+= mydict[concept]
    info = math.log(hypo,2)/FenMu
    return 1-info


with open('count.txt', 'a') as f:
    for k,v in mydict.items():
        print(k,v)
        line = k +' ' +str(v)+'\n'
        f.write(line)

