# -*- coding: utf-8 -*-
'''
@author: Yalei Meng
@contact: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.

@DateTime: Created on 2018/4/8，at 19:22
@desc:
'''
with open('E:/fanyici.txt', 'r', encoding='utf-8')as f:
    data = f.readlines()
    print(len(data))
    for line in data:
        if not line.strip():
            continue
        words = line.strip().split(' ')[:-1]
        if len(words) ==2:
            print(words[0],words[1])

