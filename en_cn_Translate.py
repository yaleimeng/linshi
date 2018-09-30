# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/9/27, at 上午 10:37 by PyCharm '''

import time
from selenium import webdriver

driver = webdriver.Chrome()  # Chrome浏览器的驱动


def Baidu_translate(sentence):
    driver.get('http://fanyi.baidu.com/')
    in_box = driver.find_element_by_css_selector('div textarea.textarea')
    in_box.clear()
    in_box.send_keys(sentence)
    try:
        driver.implicitly_wait(1)  # 隐式等待，如果没有发现元素，就等待1秒
        out_box = driver.find_element_by_css_selector('div.output-wrap span')
    except:
        time.sleep(0.5)
        out_box = driver.find_element_by_css_selector('div.output-wrap span')
    return out_box.text  # 返回翻译结果


def Youdao_translate(sentence):
    driver.get('http://fanyi.youdao.com/')
    in_box = driver.find_element_by_css_selector('div textarea#inputOriginal')
    in_box.clear()
    in_box.send_keys(sentence)
    try:
        driver.implicitly_wait(1)  # 隐式等待，如果没有发现元素，就等待1秒
        out_box = driver.find_element_by_css_selector('div#transTarget span')
    except:
        time.sleep(0.5)
        out_box = driver.find_element_by_css_selector('div#transTarget span')
    return out_box.text  # 返回翻译结果


def Sogou_translate(sentence):
    driver.get('http://fanyi.sogou.com/')
    in_box = driver.find_element_by_css_selector('#sogou-translate-input')
    in_box.clear()
    in_box.send_keys(sentence)
    # in_box.send_keys(K.Keys.RETURN)
    time.sleep(0.5)  # 显式等待。因为元素本来就有。但一直取不到内容比较麻烦
    out_box = driver.find_element_by_css_selector('div.to-text')
    return out_box.text  # 返回翻译结果


# def Google_Eng2Chi(sentence):  # 默认英文可以翻译到中文
#     driver.get('https://translate.google.cn/')
#     in_box = driver.find_element_by_css_selector('textarea#source')
#     in_box.clear()
#     in_box.send_keys(sentence)
#     time.sleep(0.5)  # 显式等待。
#     out_box = driver.find_element_by_css_selector('span#result_box')
#     return out_box.text  # 返回翻译结果
#
#
# def Google_Chi2Eng(sentence):  # 中文翻译为英文需要注意
#     driver.get('https://translate.google.cn/#zh-CN/en/')
#     in_box = driver.find_element_by_css_selector('textarea#source')
#     in_box.clear()
#     in_box.send_keys(sentence)
#     time.sleep(0.5)  # 显式等待。
#     out_box = driver.find_element_by_css_selector('span#result_box')
#     return out_box.text  # 返回翻译结果


def equal_forms(sentence):
    my_dict = {Baidu_translate, Sogou_translate, Youdao_translate}

    for inside in my_dict:
        mid = inside(sentence)
        if not mid:
            print('中间结果为空！', inside)
            continue
        #time.sleep(0.2)
        for outside in my_dict:
            final = outside(mid)
            possible.add(final)
            #time.sleep(0.2)

possible = set()

with open('first500.txt', 'r', encoding='utf-8') as fr, open(
          'New500.txt', 'a', encoding='utf-8') as fw:
    order = 4068                  # 设置序号初始值！！
    for row in fr.readlines():    # 必要时，这里可设置切片！！
        row = row.strip()
        if not row:
            continue
        if possible:   possible.clear()  # 先清除之前保存的内容
        possible.add(row)  # 先将当前问句加入。避免后续重复的行
        equal_forms(row)  # 执行翻译工作。

        fw.write('{}\t{}\n'.format(str(order), row))
        for one in possible:
            if not one:  # 如果保存的是空字符串。剔除掉
                continue
            print(order, one)
            fw.write('{}\t{}\n'.format(str(order), one))
        order += 1

driver.close()
