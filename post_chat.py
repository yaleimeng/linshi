# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/4/18, at 上午 10:09 by PyCharm '''
import requests


#web = 'http://im.openmoa.cn:5100/'              # CS 引擎。。:build harry 来使脚本生效。
web = 'http://im.openmoa.cn:5200/'             # FAQ引擎。。 /reload 来更新数据。


myform =  {'userID':'00fg','question':'怎样申请高新技术企业？', #用户id、问题内容。
          # 'answer':'','belief':1.0,'block':'','Q_choice':[] # 答案、置信度、语义块、备选疑似问题
}

r = requests.post(web,myform,timeout=5)
print(r.json())
