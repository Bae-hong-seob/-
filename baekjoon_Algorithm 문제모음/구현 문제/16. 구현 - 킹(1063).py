# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:12:10 2022

@author: bhs89
"""

import sys

def input():
    return sys.stdin.readline().strip()

king, stone, N = input().split()
king, stone = list(king), list(stone)
N = int(N)
row =[str(i) for i in range(1,9)]
column = [i for i in 'ABCDEFGH']

#king, stone 인덱스로 관리
king = [row.index(king[1]),column.index(king[0])]
stone = [row.index(stone[1]),column.index(stone[0])]

def move(how,row,column):
    if how == 'R':
        column+=1
    elif how == 'L':
        column-=1
    elif how == 'B':
        row-=1
    elif how == 'T':
        row+=1
    elif how == 'RT':
        column+=1
        row+=1
    elif how == 'LT':
        column-=1
        row+=1
    elif how == 'RB':
        column+=1
        row-=1
    elif how == 'LB':
        column-=1
        row-=1
    
    return row,column

for i in range(N):
    # 움직이는 방향
    go = input()
    go_row, go_column = move(go,king[0],king[1])
    
    # go_row, go_column 가 stone과 같은 위치 인 경우
    if go_row == stone[0] and go_column == stone[1]:
        go_stone_row, go_stone_column = move(go,stone[0],stone[1])
        
        # 돌 먼저 옮기고 킹 옮기고
        # 이때 돌이 체스판 안에 있어야함
        if 0 <= go_stone_row < 8 and 0 <= go_stone_column < 8 and 0 <= go_row < 8 and 0 <= go_column < 8:
            stone[0], stone[1] = go_stone_row, go_stone_column
            king[0], king[1] = go_row, go_column
        else:
            continue
    # go_row, go_column에 stone이 없는 경우
    else:
        if 0 <= go_row < 8 and 0 <= go_column < 8:
            king[0], king[1] = go_row, go_column
        else:
            continue

# 현재 row, column은 index -> 숫자
king[1], king[0] = row[king[0]], column[king[1]]
stone[1], stone[0] = row[stone[0]], column[stone[1]]

print(''.join(king))
print(''.join(stone))