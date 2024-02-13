import math

from itertools import permutations

def is_primenumber(x):
    if x==0 or x==1: #0과1은 소수가 아니다
        return False
    
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: #소수가 아닌 경우
            return False
    return True

def solution(numbers):
    
    # 완전탐색 가능 확인
    count = 0
    for i in range(1, 8):
        count+=math.factorial(i)
    #print(count) #numbers길이 최대 7이므로 총 경우의 수 5913개.
    
    candidates = set()
    for i in range(1, len(numbers)+1):
        for candidate in permutations(numbers, i):
            number = int(''.join(candidate))
            candidates.add(number)
            
    return sum([is_primenumber(candidate) for candidate in candidates])