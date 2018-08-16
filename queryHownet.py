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
# 单词id 最大值231090,日期2018-8-15     最小值3378
with open('Full_how.txt', 'a', encoding='utf-8') as full, open(
        'Mini_how.txt', 'a', encoding='utf-8')as mini:
    for i in range(6000,6012):  # 这里只需要修改初始数字（会执行）。终止数不包含。
        num = 6 - len(str(i))
        word_id = '0' * num + str(i)
        params = {'apiKey': 'vcyq8fmq', 'unitId': word_id}
        try:
            r = rq.post(nlp_url, data=params)
            full.write(r.text + '\n')
            Chi_word = re.findall(cwrg, r.text)
            pos = re.findall(posrg, r.text)
            info = re.findall(defrg, r.text)
            if Chi_word and pos and info:       # 对匹配到的字符串做格式化处理，提取有效部分
                cw,tag = Chi_word[0][4:-1],pos[0][4:-1].split()[0]
                DEF = info[0].replace('{', ',').replace('}', '')[5:-1]
                print(word_id, cw + '\t\t' + tag + '\t\t' + DEF)
                #mini.write(cw + '\t\t' + tag + '\t\t' + DEF + '\n')
        except:
            break           # 结束循环，报告异常，以便重新开始
        finally:
            time.sleep(random.uniform(0.8, 3))
