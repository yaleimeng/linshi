# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/8/15, at 上午 09:43 by PyCharm '''

import time, random
import requests as rq

bag = set()
keys = ['vcyq8fmq','2t1ojsgi']
url = 'http://yuzhinlp.com/api/getWordAttribute.do'
with open('D:/how_Def0819.txt', 'r', encoding='utf-8') as fd, open(
        'w2s.txt', 'r', encoding='utf-8') as fs,open(
        'Others.txt', 'a', encoding='utf-8') as fw   :
    for line in fd.readlines():       # 读取已收集的知网词汇id，后续如果重复。就不再加入
        if line.strip():
            row = tuple(line.split())
            bag.add(row)
    print('现存不重复的义项数量：',len(bag))
    for num,line in enumerate(fs.readlines(),1):
        sentence = line.strip()
        param = {'apiKey': random.choice(keys), 'input': sentence, }   #    vcyq8fmq
        r = rq.post(url, data=param, )
        try:
            cj = r.json()
            if cj['success']:
                for word in cj['success'][:-1]:  # 这里是一句话中所有单词的数据。有些可能会重复
                    row = (word['unitId'], word['expressionInSentence'], word['partOfSpeech'], word['unitDefination'])
                    if row in bag:
                        continue
                    bag.add(row)     # 让集合里保存所有信息，这样能减少冗余
                    print(row)
                    wid, wself, wpos, wdef = row
                    fw.write(wid + '\t' + wself + '\t' + wpos + '\t' + wdef + '\n')
        except:
            print('抽取过程出错！'+'===='*5 )
            continue
        finally:
            print('==='*5,'第%d行已处理完毕！'%num)
            time.sleep(random.uniform(0.5, 1.3))

    print('\n恭喜，爬取完毕。总共收集不重复义项数量：', len(bag))



sentence = '今晚上我请你吃饭'
param = {'apiKey': '2t1ojsgi', 'input': sentence, }   #    vcyq8fmq    2t1ojsgi
r = rq.post(url, data=param, )
cj = r.json()
if cj['success']:
    for word in cj['success'][:-1]:  # 这里是一句话中所有单词的数据。有些可能会重复
        row = (word['unitId'], word['expressionInSentence'], word['partOfSpeech'], word['unitDefination'])
        print(row)
