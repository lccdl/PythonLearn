#! /usr/bin/python
# coding: UTF-8

import re

# 1.写一个正则表达式，使其能同时识别下面所有的字符串：’bat’,’bit’, ‘but’, ‘hat’, ‘hit’, ‘hut’
def findPinStr():
    array = ['bat','bit', 'but', 'hat', 'hit', 'hut','sdfsdf']

    for str in array:
        rst = re.search('^[bh][aiu]t$', str, re.M|re.I)
        if rst: 
            print('match:%s' % (rst.group()))

#
def 


findPinStr()
