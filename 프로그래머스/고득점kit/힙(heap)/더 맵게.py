import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K and len(scoville)>=2:
        answer+=1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville,first + 2*second)
    
    if scoville[0] < K:
        return -1
    else:
        return answer