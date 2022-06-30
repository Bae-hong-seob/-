# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:51:42 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

N,L = map(int,input().split())

info_N = []
for i in range(N):
    info_N.append(list(map(int, input().split())))
    
move = 0
t = 0
how = 'go'

while (move != L):
    t+=1
    # 신호등 만나는지
    for i in info_N:
        # 신호등 만날경우
        if move == i[0]:
            # 빨간 불
            if 0 < t % (i[1]+i[2]) <= i[1]:
                how = 'stop'
            # 초록 불
            else:
                how = 'go'
    # 신호등 안만나는 경우
    if how == 'go':
        move+=1
    
print(t)