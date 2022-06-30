# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:39:10 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

def expand_digit(num,depth,_47list):
    
    if depth == 10:
        return
    add_4 = (num*10) +4
    add_7 = (num*10) +7
    _47list.append(add_4)
    _47list.append(add_7)
    
    expand_digit(add_4, depth+1, _47list)
    expand_digit(add_7, depth+1, _47list)
    
    return _47list

A , B = map(int, input().split())

_47list = []

_47list = expand_digit(0, 1, _47list)
_47list.sort()


for i in _47list:
    if i >= A:
        start_idx = _47list.index(i)
        break
    else:
        start_idx = -1
        
for i in reversed(_47list):
    if i <= B:
        end_idx = _47list.index(i)
        break
    else:
        end_idx = -1

try:
    if start_idx == -1 or end_idx == -1 or start_idx > end_idx:
        print(0)
    else:
        count = end_idx - start_idx + 1
        print(count)
except:
    print(0)