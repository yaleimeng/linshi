# -*- coding: utf-8 -*-
'''
@author: Yalei Meng
@contact: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.

@DateTime: Created on 2018/5/3，at 18:47
@desc:
'''
#
# with open('cilin.txt', 'r', encoding='gbk') as f,open('nums.txt','a') as fw:
#     for line in f.readlines():
#         res = line.split()
#         code = res[0]  # 词义编码
#         words = res[1:]  # 同组的多个词
#         new_line = code +' '+str(len(words))+'\r\n'
#         print(new_line)
#         fw.write(new_line)
head = set()

with open('cilin.txt', 'r', encoding='gbk') as f:
    for line in f.readlines():
        res = line.split()
        code = res[0]  # 词义编码
        fathers = [code[:1],code[:2],code[:4]]
        head.update(fathers)
    fatherlist = sorted(list(head))
    for ele in fatherlist:
        print(ele)



print('所有叶子编码统计完毕')