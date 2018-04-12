# -*- coding: utf-8 -*-
'''
@author: Yalei Meng
@contact: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.

@DateTime: Created on 2018/4/8，at 19:22
@desc:
'''
# # 将原来的一行多个次，重写为一行一对。。然后再考虑去除彼此重复的问题。
# with open('E:/fanyici.txt', 'r', encoding='utf-8'
#           )as f,open('E:/newFan.txt', 'a', encoding='utf-8'
#           )as fw:
#     data = f.readlines()
#     for line in data:
#         if not line.strip(): # 遇到空行跳过
#             continue
#         words = line.strip().split(' ')[:-1]
#         if len(words)<2:
#             continue
#         if len(words) == 2:
#             fw.write(words[0]+'\t'+words[1]+'\n')
#         else:
#             for yi in words[1:]:
#                 fw.write(words[0] + '\t' +yi+'\n')


# 找出彼此重复项
with open('E:/single.txt', 'r', encoding='utf-8'
          )as f:
    data = f.readlines()
    seen = set()
    chongfu = set()
    for line in data:
        if not line.strip():  # 遇到空行跳过
            continue
        words = line.strip().split()
        if words[0]+'\t'+words[1] not in seen and words[1]+'\t'+words[0] not in seen:
            seen.add(words[0]+'\t'+words[1])
            seen.add(words[1]+'\t'+words[0])
            print(words[1], words[0])
        else:  # 已经出现过的,打印出来。这些是双向反义词。
            chongfu.add(words[0] + '\t' + words[1])
            chongfu.add(words[1] + '\t' + words[0])

    #
    # print('=='*30)
    # for ele in seen-chongfu:   # 差集部分，这些是只出现了一次的反义词对。
    #     print(ele)
