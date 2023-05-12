import heapq

def solution(s):
    s_max = list(map(int,s.split(' ')))
    s_min = list(map(int,s.split(' ')))
    s_max = [i*(-1) for i in s_max]
    heapq.heapify(s_max)
    heapq.heapify(s_min)
    
    print(s_max)
    print(s_min)
    
    answer_max = heapq.heappop(s_max)
    answer_min = heapq.heappop(s_min)
    
    answer = [str(answer_min), ' ' ,str((-1)*answer_max)]
    return ''.join(answer)