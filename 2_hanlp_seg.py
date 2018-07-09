# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/6/29, at 上午 10:23 by PyCharm '''

from pyhanlp import *


if __name__ == '__main__':
    CRFSeger = JClass("com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer")
    analyzer = CRFSeger().enableCustomDictionary(True)  # 词法分析器，可以用分词器、词性标注、NER三者的方法

    f = open('std_wiki_00', 'r', encoding='utf-8')
    target= open('gb02.txt', 'w', encoding='utf-8')
    print('已经打开文件....')

    lineNum = 1
    for line in f:
        if not line.strip():
            continue
        print('---processing ', lineNum, ' article---')
        line = HanLP.convertToSimplifiedChinese(line.strip())  # 对原始行做简繁转换。 这一步不会出错，都能打印。
        words =  analyzer.segment(line.encode('utf-8', 'ignore').decode('utf-8'))  # 分词结果经常是无法打印。
        new_words = [term.encode('utf-8', 'ignore').decode('utf-8') for term in words]
        newline = ' '.join(new_words).replace('  ','')
        print(newline)
        target.write(newline)
        lineNum += 1

    f.close()
    target.close()
    print('well done.恭喜，已全部完成。')