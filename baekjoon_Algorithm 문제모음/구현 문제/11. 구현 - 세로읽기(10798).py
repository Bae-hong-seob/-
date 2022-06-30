# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:37:52 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

_sentences = []
for i in range(5):
    _sentences.append(input())
    
sum_of_sentences = ''
error_num = 0

for i in range(15):
    # 첫번쨰 sentence
    try:
        sum_of_sentences += _sentences[0][i]
    except:
        error_num +=1
    # 두번째 sentence
    try:
        sum_of_sentences += _sentences[1][i]
    except:
        error_num +=1
    # 세번째 sentence
    try:
        sum_of_sentences += _sentences[2][i]
    except:
        error_num +=1
    # 네번째 sentence
    try:
        sum_of_sentences += _sentences[3][i]
    except:
        error_num +=1
    # 다섯번째 sentence
    try:
        sum_of_sentences += _sentences[4][i]
    except:
        error_num +=1

print(sum_of_sentences)