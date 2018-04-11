# -*- coding: utf-8 -*-
'''
@author: Yalei Meng
@contact: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.

@DateTime: Created on 2018/4/10，at 21:35
@desc:
'''
import chardet
import requests as rq
from bs4 import BeautifulSoup as bs
import time, random, re


head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.5.2000',
        #'Referer':'http://fyc.5156edu.com/fyc.php',
        'Cookie':'Hm_lvt_6dc7d7b0834abc6bcdc42ba4c22e18d0=1523176481',
        'X-DevTools-Emulate-Network-Conditions-Client-Id':'53fb965d-3add-4c7a-ae97-4fb8d28f72e2'
        }

def get_pinyin(page):
    r = rq.get(page,headers=head,timeout=10)
    r.encoding = 'gb18030'
    soup = bs(r.text, 'lxml')
    if not soup.select('td.font_22'):
        return ''
    else:
        zi = soup.select('td.font_22')[0].text
        yin = soup.select('td.font_14')[0].text.split(',')
        for ele in yin:
            real = ele.split(' ')[0]
            zi =zi + ' '+real
        print(zi)
        return zi

urls = ['http://xh.5156edu.com/html3/{}.html'.format(str(i)) for i in range(1, 22526)]

#line = get_pinyin(urls[6215])


with open('E:/All_PinYin.txt', 'a', encoding='utf-8')as f:
    for url in urls:
        print(url)
        line = get_pinyin(url)
        time.sleep(0.8)
        if not line:
            continue
        f.write(line+'\r\n')
