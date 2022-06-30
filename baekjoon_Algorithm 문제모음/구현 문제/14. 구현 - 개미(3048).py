# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:51:16 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

N1,N2 = map(int, input().split())

ant1 = list(input())
ant2 = list(input())
ant1.reverse()

T = int(input())

ant_dict = dict()

for i in ant1:
    ant_dict[i] = 'R'

for i in ant2:
    ant_dict[i] = 'L'

ants = []
ants.extend(ant1)
ants.extend(ant2)

for i in range(T):
    record = []
    for i in range(N1+N2-1):
        if ant_dict[ants[i]] == 'R' and ant_dict[ants[i+1]] == 'L':
            record.append(i)
    
    for i in record:
        temp = ants[i+1]
        ants[i+1] = ants[i]
        ants[i] = temp

print(''.join(ants))

'''정답
_ = map(int, input().split())
g1 = [{'group': 1, 'name': ant} for ant in input()][::-1]
g2 = [{'group': 2, 'name': ant} for ant in input()]
ants = g1 + g2
T = int(input())

for _ in range(T):
    i = 0
    while i < len(ants) - 1:
        if ants[i]['group'] < ants[i + 1]['group']:
            ants[i], ants[i + 1] = ants[i + 1], ants[i]
            i += 1
        i += 1
        
print("".join([ant['name'] for ant in ants]))
'''