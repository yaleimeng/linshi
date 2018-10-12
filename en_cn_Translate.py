# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/9/27, at 上午 10:37 by PyCharm '''

import time
from selenium import webdriver
from retry import retry


@retry(tries=16, delay=0.5)
def crawl_no_right(sentence, site, in_selector, out_selector, waiting=1.0, needF5=False):
    driver.get(site)
    if needF5:
        driver.refresh()  # 如果需要刷新，就刷新一下
    in_box = driver.find_element_by_css_selector(in_selector)
    in_box.send_keys(sentence)
    driver.implicitly_wait(waiting)  # 隐式等待，如果没有发现元素，就等待1秒
    out_box = driver.find_element_by_css_selector(out_selector)
    return out_box.text  # 返回翻译结果


def Baidu_translate(sentence):
    site = 'http://fanyi.baidu.com/'
    in_box, out_box = 'div textarea.textarea', 'div.output-wrap span'

    return crawl_no_right(sentence, site, in_box, out_box, 1)


def Youdao_translate(sentence):
    site = 'http://fanyi.youdao.com/'
    in_box, out_box = 'div textarea#inputOriginal', 'div#transTarget span'
    return crawl_no_right(sentence, site, in_box, out_box)


def iCiba_translate(sentence):
    site = 'http://fy.iciba.com/'
    in_box, out_box = 'div.textarea-wrap textarea', 'div.res-sentence span'
    return crawl_no_right(sentence, site, in_box, out_box, 4, needF5=True)  #


def Tencent_translate(sentence):
    site = 'https://fanyi.qq.com/'
    in_box, out_box = 'div.textpanel-source textarea', 'span.text-dst'
    return crawl_no_right(sentence, site, in_box, out_box)


@retry(tries=15, delay=0.5)
def crawl_with_right(sentence, site, in_selector, out_selector, waiting=0.5, needF5=False):
    driver.get(site)
    if needF5:
        driver.refresh()  # 如果需要刷新，就刷新一下
    in_box = driver.find_element_by_css_selector(in_selector)
    in_box.send_keys(sentence)
    time.sleep(waiting)  # 显式等待。因为元素本来就有。但一直取不到内容比较麻烦
    out_box = driver.find_element_by_css_selector(out_selector)
    return out_box.text  # 返回翻译结果


def Sogou_translate(sentence):
    site = 'http://fanyi.sogou.com/'
    in_box, out_box = '#sogou-translate-input', 'div.to-text'

    return crawl_with_right(sentence, site, in_box, out_box, 1.2)


def Google_Eng2Chi(sentence):
    site = 'https://translate.google.cn/'  # 默认网址英文可以翻译到中文
    in_box, out_box = 'textarea#source', 'span#result_box'
    return crawl_with_right(sentence, site, in_box, out_box, 1.2)


# def Bing_translate(sentence):  # 必应翻译爬虫无法得到翻译结果文本
#     '''请求地址 https://cn.bing.com/ttranslate?&category=&IG=AD6440EC7C08461493E5EA457793877B&IID=translator.5036.5
#     category为空。IG是随机字符串，IID是可读字符串
#     post内容为：
#     - text:我不喜欢动画片。
#     - from:zh-CHS
#     - to:en
#     '''
#
#     site = 'http://cn.bing.com/translator/'
#     in_box, out_box = 'div.t_inblock textarea', 'div.t_outblock textarea'
#     return crawl_with_right(sentence, in_box, out_box)
#

def equal_forms(sentence):
    my_dict = [Baidu_translate, Tencent_translate, iCiba_translate,
               Sogou_translate, Youdao_translate, Google_Eng2Chi, ]
    for inside in my_dict:
        mid = inside(sentence)
        if mid:
            possible.add(mid)
        else:
            print('翻译结果为空！', inside)


chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_opt.headless=True
chrome_opt.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_opt)

possible = set()

# 单个翻译引擎测试
# zi = 'you are so clever that nobody can fool you.'
# possible.add(iCiba_translate(zi))
# print(possible)


with open('Haowenti.txt', 'r', encoding='utf-8') as fr, open(
        'NewData.txt', 'a', encoding='utf-8') as fw:
    order = 18911  # 设置序号初始值！！
    for row in fr.readlines()[12911:]:  # 必要时，这里可设置切片！！
        row = row.strip()
        if not row:
            continue
        if possible:   possible.clear()  # 先清除之前保存的内容
        equal_forms(row)  # 执行翻译工作。

        for one in possible:
            if not one:  # 如果保存的是空字符串。剔除掉
                continue
            print(order, one, sep='\t')
            fw.write('{}\t{}\n'.format(str(order), one))
        order += 1

driver.close()
