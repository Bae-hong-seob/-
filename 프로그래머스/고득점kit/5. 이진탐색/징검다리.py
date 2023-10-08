from itertools import permutations
from collections import deque

def solution(distance, rocks, n):
    original_list = list(permutations(rocks, len(rocks)-n))
    unique_list = list(set(tuple(sorted(sublist)) for sublist in original_list))
    unique_list.sort()
    
    answer = 0
    for candidate in unique_list:
        dq = deque(candidate)
        dq.appendleft(0)
        dq.append(distance)
        distances = [dq[i]-dq[i-1] for i in range(1,len(dq))]
        answer = max(answer, min(distances))
    
    return answer

def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    start,end = 1, distance
    answer = 0
    
    while start <= end:
        mid = (start+end)//2 # mid가 각 바위 사이의 거리 중 최소값이여야함.
        del_rocks, pivot = 0,0
        min_distance = distance
        
        for rock in rocks:
            if rock-pivot < mid: #두 바위 사이 거리가 mid값 보다 작으면 바위 제거
                del_rocks+=1
            else:
                min_distance = min(min_distance, rock-pivot)
                pivot = rock # peviot 옮기기
                
            if del_rocks > n:
                break
                
            
        if del_rocks > n: # 바위를 너무 많이 제거하면 mid를 낮춰야지.
            end = mid-1
        else:
            answer = min_distance
            start = mid+1
            
    return answer