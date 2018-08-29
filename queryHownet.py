# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/3/6, at 上午 09:10 by PyCharm '''
import time, random,re

import requests as rq

# sentence = '出生地在哪儿'
# payload = {'apiKey': 'vcyq8fmq','input':sentence}
# text_url = 'http://yuzhinlp.com/api/call_chn.do'
# r = rq.post(text_url,data=payload)


cwrg = re.compile('W_C=.*?,')
posrg = re.compile('G_C=.*?,')
defrg = re.compile('DEF={.*?,')
nlp_url = 'http://yuzhinlp.com/api/call_UnitIdApi.do'
keys = ['2t1ojsgi','vcyq8fmq']  # API key列表。可随机选择
# 单词id 最大值231090,日期2018-8-15     最小值3378
with open('NotSeen.txt','r') as fr, open(
        'Mini_how.txt', 'a', encoding='utf-8')as mini:
    task = []                   # 列表能保证爬取顺序
    for line in fr.readlines():
        task.append(line.strip())

    for wid in task:
        params = {'apiKey': random.choice(keys), 'unitId': wid}
        try:
            r = rq.post(nlp_url, data=params)
            # full.write(r.text + '\n')
            Chi_word = re.findall(cwrg, r.text)
            pos = re.findall(posrg, r.text)
            info = re.findall(defrg, r.text)
            if Chi_word and pos and info:       # 对匹配到的字符串做格式化处理，提取有效部分
                cw,tag = Chi_word[0][4:-1],pos[0][4:-1].split()[0]
                DEF = info[0].replace('{', ',').replace('}', '')[5:-1]
                print(wid, cw + '\t' + tag + '\t' + DEF)
                mini.write(wid+'\t'+cw + '\t' + tag + '\t' + DEF + '\n')
        except:
            break           # 结束循环，报告异常，以便重新开始
        finally:
            time.sleep(random.uniform(0.5, 1))
