# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:06:00 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

H, M = map(int, input().split())

modify_H = H
modify_M = M - 45

if modify_M < 0:
    # H를 1 줄이고, 60분에서 줄이기
    modify_M = 60 - abs(modify_M)
    modify_H -=1
    # 0시 에서 빼기 -> 23시
    if modify_H < 0:
        modify_H = 23

print(modify_H,modify_M)