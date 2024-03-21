from collections import Counter
from itertools import combinations

def solution(weights):
    counter = Counter(weights)
    answer = 0
    for key,value in counter.items():
        #1:1, 1:2, 2:3, 3:4 비율만 보면 됨
        answer+=(value*(value-1)/2) #nC2
        answer+=counter[key*2]*value
        answer+=counter[key*3/2]*value
        answer+=counter[key*4/3]*value
                
    
    return answer
