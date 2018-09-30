# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/9/30, at 下午 02:23 by PyCharm '''

import MySQLdb as db

link = db.connect(host='ask.mo.cn', user='meng.yalei', password='123456',
                  db='ai_database', port=3306, )

cur = link.cursor()
cur.execute('SELECT * FROM knowlege_FAQ')
mydata = cur.fetchall()
for line in mydata:
    print(line)

link.close()
