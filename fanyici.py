# -*- coding: utf-8 -*-
'''
@author: Yalei Meng
@contact: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.

@DateTime: Created on 2018/4/4，at 21:50
@desc:
'''
import requests as rq
from bs4 import BeautifulSoup as bs
import time, random, re


yisi = re.compile('\)?.*?\(')
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.5.2000',
        #'Referer':'http://fyc.5156edu.com/fyc.php',
        'X-DevTools-Emulate-Network-Conditions-Client-Id':'030de2fa-3780-4630-b1f6-51f36fde051d'
        }

def get_inverse(page):
    fan = ''
    r = rq.get(page,headers=head,timeout=10)
    r.encoding = 'gb2312'
    soup = bs(r.text, 'lxml')
    tag = soup.find_all('td', width='88%')
    if not tag:
        return ''
    clean = tag[0].text.strip().replace('\n', '')
    word = clean.split('(')[0]
    fan += word + ' '
    wlist = yisi.findall(tag[1].text.strip().replace('\n', ''))
    if not wlist:
        fan += tag[1].text.strip()
    else:
        for w in wlist:
            if w.find(')') > 0:
                fan += w.strip().split(')')[-1][:-1]
            else:
                fan += w[:-1]
    print(fan+' '+page)
    return  fan+' '+page


urls = ['http://fyc.5156edu.com/html/{}.html'.format(str(i)) for i in range(101, 7498)]

with open('E:/Fanyi.txt', 'a', encoding='utf-8')as f:
    for url in urls:
        line = get_inverse(url)
        if not line:
            continue
        f.write(line)
        f.write('\r\n')
        time.sleep(0.5)
