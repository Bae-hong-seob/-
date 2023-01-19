import math

def solution(clothes):
    match = dict()
    
    for i in clothes: #dictionary 생성
        match[i[1]] = 0
    
    for i in clothes:
        match[i[1]] += 1
    answer = 1
    
    for i in match:
        answer*=(match[i] + 1)
    
    return answer - 1