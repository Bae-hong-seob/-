from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answers = []
    for length in course: #최대 10개 오름차순으로 정렬되어있음
        menu2number = defaultdict(int)
        for order in orders: #최대 20 -> 200번 반복
            candidates = list(combinations(order,length)) # 최대 10 C 5 = 30,240개. * 200 = 6백만.
            for candidate in candidates:
                candidate = tuple(sorted(candidate))
                menu2number[candidate]+=1
        
        if menu2number.values():
            candidate_number = max(menu2number.values())
        else:
            candidate_number = 0
            
        if candidate_number < 2:
            continue
            
        for key,value in menu2number.items():
            if candidate_number == value and value>=2:
                #print(key, value)
                answers.append(''.join(key))
                
    return sorted(answers)