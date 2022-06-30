#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:54:28 2022

@author: baehongseob
"""

import sys

def input():
    return sys.stdin.readline()

N, K = map(int, input().split())
coins = []
result = 0

for i in range(N):
    coin = int(input())
    coins.append(coin)
        
while(K != 0): #K가 0이 될때까지 진행
    for i in range(N):
        if (K % coins[i]) == K:
            div_index = i-1 #현재 coin으로는 나눌 수 없으므로 이전 값 저장
            break
        else:
            div_index = i
    count_coin = K // coins[div_index]
    result += count_coin
    
    K = K - (count_coin * coins[div_index])
    
print(result)
