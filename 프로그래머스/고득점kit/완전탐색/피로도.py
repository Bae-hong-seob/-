import math
from itertools import permutations, product, combinations, combinations_with_replacement

def solution(k, dungeons):
    #print(math.factorial(8)*8) #완전탐색 시간 복잡도 확인
    candidates = list(permutations(dungeons))
    answer = 0
    for candidate in candidates:
        new_k, new_answer = k, 0
        for min_value, cost in candidate: #해당 경우의 수 탐색
            if new_k >= min_value:
                new_answer+=1 #던전 탐험
                new_k-=cost
            else:
                break
        answer = max(answer, new_answer) #최대 던전 수로 update

    return answer