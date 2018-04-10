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
        'X-DevTools-Emulate-Network-Conditions-Client-Id':'20e5e139-3fbb-453d-8666-adaaa7200972'
        }

def get_pinyin(page):
    print(page)
    r = rq.get(page,headers=head,timeout=10)
    r.encoding = 'gbk'
    soup = bs(r.text, 'lxml')
    if not soup.select('td.font_22'):
        return
    else:
        zi = soup.select('td.font_22')[0]
        yin = soup.select('td.font_14')[0]
        print(zi,'\n',yin)




urls = ['http://xh.5156edu.com/html3/{}.html'.format(str(i)) for i in range(1, 22526)]

get_pinyin(urls[2200])