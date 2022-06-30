# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:21:19 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()


''' 0이 배, 1이 등 -> 0이 윷, 1이 모
도 : A = 1
개 : B = 2
걸 : C = 3
윷 : D = 0
모 : E = 4
'''
for i in range(3):
    count = list(map(int,input().split()))
    sum_of_count = sum(count)
    
    #윷
    if sum_of_count == 0:
        print('D')
    #뒷면 한개 - 걸
    elif sum_of_count == 1:
        print('C')
    elif sum_of_count == 2:
        print('B')
    #도
    elif sum_of_count == 3:
        print('A')
    #모
    elif sum_of_count == 4:
        print('E')