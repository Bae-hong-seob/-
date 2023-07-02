# def solution(food_times, k):
#     if sum(food_times) < k:
#         return -1
#     i = 0
#     for index in range(k):
#         if sum(food_times) == 0: # 음식 다 먹은 경우
#             return -1
#         else:
#             index = index % len(food_times)
#             # 지금 먹을 음식 index 지정
#             while(True):
#                 if food_times[index] == 0:
#                     index = (index+1) % len(food_times)
#                 else:
#                     break 
#             food_times[index]-=1
        
#     return ((index+1) % len(food_times)) + 1 # 음식 번호는 1부터

# import heapq

# def solution(food_times, k):
#     if sum(food_times) <= k: # 음식 다 먹어도 시간이 남을 때
#         return -1
    
#     hq = []
#     for index, time in enumerate(food_times):
#         heapq.heappush(hq,[time, index+1])
    
#     if k > hq[0][0]*len(hq): # 음식 하나 다 먹을 수 있을 때
#         while(k > hq[0][0]*len(hq)):
#             how_many_circle = k // len(hq)
#             k -= hq[0][0]*len(hq)
#             heapq.heappop(hq)
            
#             # 각 음식 먹는데 남은 시간은 circle 수(몫) 만큼만 빠짐.
#             hq = [[i[0]-how_many_circle, i[1]] for i in hq]
#             heapq.heapify(hq)
#         hq = sorted(list(hq), key = lambda x:x[1]) #index 기준으로 재정렬
#         return hq[len(hq)%k][1]
    
#     else: # 음식 하나도 다 먹지 못할 때
#         return (k % len(food_times)) +1 # 음식 번호는 1번부터

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if k >= sum(food_times):
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    
    return result[(k-sum_value)%length][1]