# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/4/12, at 下午 04:32 by PyCharm '''

import requests as rq
from bs4 import BeautifulSoup as bs
import time, random, re

juzi = '张三昨天告诉李四这个事实。'

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.5.2000',
    'Referer': 'https://www.ltp-cloud.com/demo/', }

def get_yicuntu(wenti):
    form_data = {'api_key': 'b9D0w08oEOkGTAsF1sxfJK6DOXCQtECRtlSlCqlA',
                 'pattern': 'all',
                 'format': 'json',
                 'text': wenti,
                 'hasContain': '''function (val){
                        for(var i = 0 ; i < this.length ;   i){
                            if(this[i] == val) return true ;
                        }
                        return false ;
                    }'''
                 }
    page = 'https://api.ltp-cloud.com/analysis/'
    r = rq.post(page, headers=head, data=form_data, timeout=8)
    raw = r.json()
    for zidian in raw[0][0]:
        print(zidian)

get_yicuntu(juzi)

new = '''[[[
{'id': 0, 'ne': 'O', 'arg': [], 'relate': 'ATT', 'semrelate': 'Poss', 'semparent': 1, 'parent': 1, 'cont': '工程', 'sem': [{'id': 0, 'parent': 1, 'relate': 'Desc'}], 'pos': 'n'}, 
{'id': 1, 'ne': 'O', 'arg': [], 'relate': 'ATT', 'semrelate': 'Agt', 'semparent': 2, 'parent': 3, 'cont': '中心', 'sem': [{'id': 0, 'parent': 3, 'relate': 'Poss'}], 'pos': 'n'}, 
{'id': 2, 'ne': 'O', 'arg': [], 'relate': 'ATT', 'semrelate': 'Feat', 'semparent': 3, 'parent': 3, 'cont': '建设', 'sem': [{'id': 0, 'parent': 3, 'relate': 'Desc'}], 'pos': 'v'}, 
{'id': 3, 'ne': 'O', 'arg': [], 'relate': 'SBV', 'semrelate': 'Agt', 'semparent': 5, 'parent': 5, 'cont': '过程', 'sem': [{'id': 0, 'parent': 5, 'relate': 'Pat'}], 'pos': 'n'}, 
{'id': 4, 'ne': 'O', 'arg': [], 'relate': 'ADV', 'semrelate': 'Mann', 'semparent': 5, 'parent': 5, 'cont': '怎样', 'sem': [{'id': 0, 'parent': 5, 'relate': 'Mann'}], 'pos': 'r'}, 
{'id': 5, 'ne': 'O', 'arg': [{'id': 0, 'beg': 0, 'end': 3, 'type': 'TMP'}, {'id': 1, 'beg': 4, 'end': 4, 'type': 'ADV'}], 'relate': 'HED', 'semrelate': 'Root', 'semparent': -1, 'parent': -1, 'cont': '监督', 'sem': [{'id': 0, 'parent': -1, 'relate': 'Root'}], 'pos': 'v'},
 {'id': 6, 'ne': 'O', 'arg': [], 'relate': 'RAD', 'semrelate': 'mTone', 'semparent': 5, 'parent': 5, 'cont': '呢', 'sem': [{'id': 0, 'parent': 5, 'relate': 'mTone'}], 'pos': 'u'}, 
 {'id': 7, 'ne': 'O', 'arg': [], 'relate': 'WP', 'semrelate': 'mPunc', 'semparent': 5, 'parent': 5, 'cont': '？', 'sem': [{'id': 0, 'parent': 5, 'relate': 'mPunc'}], 'pos': 'wp'}]]]
 '''